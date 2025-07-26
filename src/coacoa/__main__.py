from __future__ import annotations

import os
import shutil
import sys
import textwrap
from pathlib import Path
from typing import Optional

import typer
from importlib_resources import files

app = typer.Typer(add_completion=False, help="CoaCoA CLI")

template_dir = files("coacoa.scaffold")

# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
def git_root() -> Optional[Path]:
    """Return git top-level dir or None if not in a git repo."""
    import subprocess

    try:
        root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return Path(root)
    except subprocess.CalledProcessError:
        return None


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def confirm(msg: str) -> bool:
    return typer.confirm(msg, default=True)


# -----------------------------------------------------------------------------
# `coacoa init` command
# -----------------------------------------------------------------------------
@app.command()
def init(
    claude_code: bool = typer.Option(
        False, "--claude-code", help="Generate CLAUDE.md at repo root"
    ),
    cline: bool = typer.Option(
        False, "--cline", help="Generate .clinerules at repo root"
    ),
):
    """
    Scaffold CoaCoA into the current git repository.
    """
    root = git_root()
    if root is None:
        typer.secho("Error: run inside a git repository", fg="red")
        sys.exit(1)

    typer.echo(f"Project root: {root}")

    # ------------------------------------------------------------------ copy
    template_dir = files("coacoa.templates")
    copy_tree(template_dir, root / ".coacoa")
    typer.secho("✓ Copied .coacoa scaffold", fg="green")

    # ------------------------------------------------------------------ .gitignore
    gi_path = root / ".gitignore"
    gi_line = ".coacoa/\n"
    if gi_path.exists():
        with gi_path.open("r+", encoding="utf-8") as fp:
            if gi_line not in fp.readlines():
                if confirm("Append .coacoa/ to .gitignore?"):
                    fp.write(gi_line)
                    typer.echo("✓ Updated .gitignore")
    else:
        gi_path.write_text(gi_line)
        typer.echo("✓ Created .gitignore")

    # ------------------------------------------------------------------ IDE helpers
    if claude_code:
        _write_helper(root, "CLAUDE.md", "claude.md")
    if cline:
        _write_helper(root, ".clinerules", "clinerules")

    typer.secho("Init complete ✔", fg="green")


# -----------------------------------------------------------------------------
def _write_helper(root: Path, filename: str, template_name: str) -> None:
    dst = root / filename
    src = files("coacoa.templates") / "ide_helpers" / template_name
    if dst.exists():
        if not confirm(f"{filename} exists. Append CoaCoA commands?"):
            typer.echo(f"Skipped {filename}")
            return
        # simple append
        dst.write_text("\n" + src.read_text(encoding="utf-8"), encoding="utf-8", append=True)
        typer.echo(f"✓ Appended {filename}")
    else:
        shutil.copy(src, dst)
        typer.echo(f"✓ Created {filename}")


if __name__ == "__main__":
    app()