from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

import typer

# --------------------------------------------------------------------------- Typer app
app = typer.Typer(add_completion=False,
                  invoke_without_command=False,
                  help="CoaCoA CLI – scaffold & helper utilities")


# --------------------------------------------------------------------------- helpers
def git_root() -> Optional[Path]:
    """Return git top-level dir or None if not inside a git repo."""
    try:
        root = (
            subprocess.check_output(
                ["git", "rev-parse", "--show-toplevel"],
                stderr=subprocess.DEVNULL,
                text=True,
            )
            .strip()
        )
        return Path(root)
    except subprocess.CalledProcessError:
        return None


def copy_tree(src: Path, dst: Path, *, force: bool = False) -> None:
    """
    Copy scaffold tree **without** nuking user edits.

    • If `dst` doesn’t exist   → normal copy.  
    • If `dst` exists          → copy only files that are missing.  
    • If a filename collides   → ask, unless `force=True`.
    """
    if not dst.exists():
        shutil.copytree(src, dst)
        return

    # merge
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            if target.exists():
                if force or confirm(f"Overwrite {target}?"):
                    shutil.copy2(item, target)
            else:
                shutil.copy2(item, target)


def confirm(msg: str) -> bool:
    return typer.confirm(msg, default=True)


# --------------------------------------------------------------------------- CLI command
@app.command("init")
def init_cmd(
    claude_code: bool = typer.Option(False, "--claude-code"),
    cline: bool = typer.Option(False, "--cline"),
):
    """
    Scaffold CoaCoA into the **current project directory**.

    • If inside a Git repo, uses the repo root.<br>
    • Otherwise, uses the present working directory.
    """
    root = git_root() or Path.cwd()

    # Confirm when not in a git repo
    if git_root() is None:
        typer.secho("⚠  Not inside a git repository.", fg="yellow")
        if not confirm(f"Proceed with workspace root '{root}'?"):
            typer.secho("Init aborted.", fg="red")
            sys.exit(1)

    typer.echo(f"Project root: {root}")

    # locate scaffold inside package
    try:
        from importlib.resources import files
    except ImportError:  # back-port for Py<3.11
        from importlib_resources import files

    scaffold_dir = Path(str(files("coacoa.scaffold")))  # Traversable → concrete Path

    # ------------------------------------------------------------------ copy toolbox
    toolbox_dst = root / ".coacoa"
    copy_tree(scaffold_dir, toolbox_dst, force=False)

    # remove IDE helper templates from the copied toolbox – they belong at project root
    ide_helpers_dst = toolbox_dst / "ide_helpers"
    if ide_helpers_dst.exists():
        shutil.rmtree(ide_helpers_dst)

    # optional user-level override
    override_yaml = root / "coacoa.yaml"
    if not override_yaml.exists() and confirm("Create editable coacoa.yaml override at project root?"):
        override_yaml.write_text("# Override CoaCoA settings here\n", encoding="utf-8")
        typer.echo("✓ Created empty override coacoa.yaml (you can git-track this)")
    typer.secho("✓ Copied .coacoa scaffold", fg="green")

    # --- update .gitignore
    gi_path = root / ".gitignore"
    gi_line = "\n.coacoa/\n"
    if gi_path.exists():
        with gi_path.open("r+", encoding="utf-8") as fp:
            lines = fp.readlines()
            if gi_line not in lines:
                if confirm("Append .coacoa/ to .gitignore?"):
                    fp.write(gi_line)
                    typer.echo("✓ Updated .gitignore")
    else:
        with gi_path.open("w", encoding="utf-8") as fp:
            fp.write(gi_line)
        typer.echo("✓ Created .gitignore")

    # --- IDE helper files
    _maybe_write_helper(root, "CLAUDE.md", "claude.md", claude_code)
    _maybe_write_helper(root, ".clinerules", ".clinerules", cline)

    typer.secho("Init complete ✔", fg="green")

from coacoa import __version__   # top of file already has __version__

@app.command("version", help="Print CoaCoA package version")
def version_cmd() -> None:
    """Show CoaCoA version and exit."""
    typer.echo(__version__)


# --------------------------------------------------------------------------- helper writer
def _maybe_write_helper(
    root: Path, filename: str, template_name: str, enabled: bool
) -> None:
    if not enabled:
        return

    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files

    src = Path(str(files("coacoa.scaffold") / "ide_helpers" / template_name))
    dst = root / filename

    # If the template is a directory (e.g., ".clinerules"), merge-copy it
    if src.is_dir():
        if dst.exists():
            # merge without nuking any user files; ask on collisions
            copy_tree(src, dst, force=False)
            typer.echo(f"✓ Updated {filename}/")
        else:
            copy_tree(src, dst, force=False)
            typer.echo(f"✓ Created {filename}/")
        return

    # Otherwise, treat it as a single file template
    if dst.exists():
        if not confirm(f"{filename} exists. Append CoaCoA block?"):
            typer.echo(f"Skipped {filename}")
            return
        with dst.open("a", encoding="utf-8") as d, src.open("r", encoding="utf-8") as s:
            d.write("\n\n")            # blank line before our block
            d.write(s.read())
        typer.echo(f"✓ Appended {filename}")
    else:
        shutil.copy(src, dst)
        typer.echo(f"✓ Created {filename}")


# --------------------------------------------------------------------------- entry-point
if __name__ == "__main__":
    app()  # important for `python -m coacoa`