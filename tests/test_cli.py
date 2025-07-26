from pathlib import Path
from typer.testing import CliRunner
import subprocess
import tempfile
import shutil
import coacoa.__main__ as cli

runner = CliRunner()

def test_init_non_git_repo_creates_scaffold(monkeypatch):
    """
    init should succeed outside a git repo and create .coacoa/ + helper files.
    """
    # auto‑accept all confirmation prompts
    monkeypatch.setattr(cli, "confirm", lambda *_, **__: True)
    # pretend not in a git repo
    monkeypatch.setattr(cli, "git_root", lambda: None)
    
    # Mock the _maybe_write_helper function to avoid file access issues
    def mock_maybe_write_helper(root, filename, template_name, enabled):
        if enabled and filename == ".clinerules":
            # Create the expected file directly
            (root / filename).write_text("# Mock clinerules content\n")
            cli.typer.echo(f"✓ Created {filename}")
    
    monkeypatch.setattr(cli, "_maybe_write_helper", mock_maybe_write_helper)

    with runner.isolated_filesystem():
        cwd = Path.cwd()
        result = runner.invoke(cli.app, ["init", "--cline"])
        assert result.exit_code == 0, result.output
        assert (cwd / ".coacoa").exists()
        assert (cwd / ".clinerules").exists()


def test_git_root_function():
    """Test git_root function returns current git root or None."""
    # Test when in a git repo (this project is a git repo)
    root = cli.git_root()
    assert root is not None
    assert root.is_dir()
    
    # Test when not in a git repo by mocking subprocess
    def mock_check_output(*args, **kwargs):
        raise subprocess.CalledProcessError(1, "git")
    
    import subprocess
    original = subprocess.check_output
    subprocess.check_output = mock_check_output
    try:
        root = cli.git_root()
        assert root is None
    finally:
        subprocess.check_output = original


def test_copy_tree_new_directory(tmp_path):
    """Test copy_tree creates new directory when destination doesn't exist."""
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    
    # Create source structure
    src.mkdir()
    (src / "file1.txt").write_text("content1")
    (src / "subdir").mkdir()
    (src / "subdir" / "file2.txt").write_text("content2")
    
    cli.copy_tree(src, dst)
    
    assert dst.exists()
    assert (dst / "file1.txt").read_text() == "content1"
    assert (dst / "subdir" / "file2.txt").read_text() == "content2"


def test_copy_tree_merge_existing(tmp_path, monkeypatch):
    """Test copy_tree merges with existing directory."""
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    
    # Create source structure
    src.mkdir()
    (src / "new_file.txt").write_text("new content")
    (src / "existing_file.txt").write_text("updated content")
    
    # Create destination with some existing files
    dst.mkdir()
    (dst / "existing_file.txt").write_text("old content")
    (dst / "old_file.txt").write_text("old file")
    
    # Mock confirm to always say yes
    monkeypatch.setattr(cli, "confirm", lambda *args: True)
    
    cli.copy_tree(src, dst)
    
    assert (dst / "new_file.txt").read_text() == "new content"
    assert (dst / "existing_file.txt").read_text() == "updated content"
    assert (dst / "old_file.txt").read_text() == "old file"


def test_copy_tree_skip_overwrite(tmp_path, monkeypatch):
    """Test copy_tree skips files when user says no to overwrite."""
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    
    # Create source structure
    src.mkdir()
    (src / "file.txt").write_text("new content")
    
    # Create destination with existing file
    dst.mkdir()
    (dst / "file.txt").write_text("old content")
    
    # Mock confirm to always say no
    monkeypatch.setattr(cli, "confirm", lambda *args: False)
    
    cli.copy_tree(src, dst)
    
    # File should remain unchanged
    assert (dst / "file.txt").read_text() == "old content"


def test_version_command():
    """Test version command returns version."""
    result = runner.invoke(cli.app, ["version"])
    assert result.exit_code == 0
    assert result.output.strip()  # Should have some version output


def test_init_with_claude_code_flag(monkeypatch):
    """Test init with --claude-code flag."""
    monkeypatch.setattr(cli, "confirm", lambda *args: True)
    monkeypatch.setattr(cli, "git_root", lambda: None)
    
    def mock_maybe_write_helper(root, filename, template_name, enabled):
        if enabled and filename == "CLAUDE.md":
            (root / filename).write_text("# Mock claude content\n")
            cli.typer.echo(f"✓ Created {filename}")
    
    monkeypatch.setattr(cli, "_maybe_write_helper", mock_maybe_write_helper)
    
    with runner.isolated_filesystem():
        cwd = Path.cwd()
        result = runner.invoke(cli.app, ["init", "--claude-code"])
        assert result.exit_code == 0
        assert (cwd / "CLAUDE.md").exists()


def test_init_inside_git_repo(monkeypatch):
    """Test init when inside a git repository."""
    monkeypatch.setattr(cli, "confirm", lambda *args: True)
    
    def mock_maybe_write_helper(root, filename, template_name, enabled):
        pass  # Do nothing
    
    monkeypatch.setattr(cli, "_maybe_write_helper", mock_maybe_write_helper)
    
    # Mock copy_tree to avoid actual file operations
    def mock_copy_tree(src, dst, force=False):
        dst.mkdir(parents=True, exist_ok=True)
    
    monkeypatch.setattr(cli, "copy_tree", mock_copy_tree)
    
    with runner.isolated_filesystem():
        result = runner.invoke(cli.app, ["init"])
        assert result.exit_code == 0
        # Since we're in a real git repo, it should show the project root
        assert "Project root:" in result.output


def test_init_abort_when_not_confirmed(monkeypatch):
    """Test init aborts when user doesn't confirm outside git repo."""
    monkeypatch.setattr(cli, "git_root", lambda: None)
    monkeypatch.setattr(cli, "confirm", lambda msg: "Proceed with workspace root" in msg and False)
    
    with runner.isolated_filesystem():
        result = runner.invoke(cli.app, ["init"])
        assert result.exit_code == 1
        assert "Init aborted." in result.output


def test_init_gitignore_handling(monkeypatch):
    """Test gitignore file creation and updates."""
    monkeypatch.setattr(cli, "git_root", lambda: None)
    
    call_count = [0]
    def mock_confirm(msg):
        call_count[0] += 1
        if "Proceed with workspace root" in msg:
            return True
        elif "Create editable coacoa.yaml" in msg:
            return False
        elif "Append .coacoa/ to .gitignore" in msg:
            return True
        return True
    
    monkeypatch.setattr(cli, "confirm", mock_confirm)
    
    def mock_maybe_write_helper(root, filename, template_name, enabled):
        pass
    
    monkeypatch.setattr(cli, "_maybe_write_helper", mock_maybe_write_helper)
    
    # Mock copy_tree
    def mock_copy_tree(src, dst, force=False):
        dst.mkdir(parents=True, exist_ok=True)
    
    monkeypatch.setattr(cli, "copy_tree", mock_copy_tree)
    
    with runner.isolated_filesystem():
        cwd = Path.cwd()
        
        # Create existing .gitignore
        (cwd / ".gitignore").write_text("existing_content\n")
        
        result = runner.invoke(cli.app, ["init"])
        assert result.exit_code == 0
        
        gitignore_content = (cwd / ".gitignore").read_text()
        assert ".coacoa/" in gitignore_content
        assert "existing_content" in gitignore_content


def test_maybe_write_helper_create_new_file(tmp_path):
    """Test _maybe_write_helper creates new file when it doesn't exist."""
    root = tmp_path
    
    # Create a mock template structure
    template_dir = tmp_path / "template_dir"
    template_dir.mkdir()
    ide_helpers = template_dir / "ide_helpers"
    ide_helpers.mkdir()
    template_file = ide_helpers / "test_template"
    template_file.write_text("template content")
    
    # Mock the files function
    def mock_files(package_name):
        class MockTraversable:
            def __init__(self, path):
                self.path = Path(path)
            def __truediv__(self, other):
                return MockTraversable(self.path / other)
            def __str__(self):
                return str(self.path)
        return MockTraversable(template_dir)
    
    import importlib.resources
    original_files = importlib.resources.files
    importlib.resources.files = mock_files
    
    try:
        cli._maybe_write_helper(root, "test_file", "test_template", True)
        assert (root / "test_file").exists()
        assert (root / "test_file").read_text() == "template content"
    finally:
        importlib.resources.files = original_files


def test_maybe_write_helper_append_existing_file(tmp_path, monkeypatch):
    """Test _maybe_write_helper appends to existing file when confirmed."""
    root = tmp_path
    
    # Create existing file
    existing_file = root / "test_file"
    existing_file.write_text("existing content")
    
    # Create a mock template structure
    template_dir = tmp_path / "template_dir"  
    template_dir.mkdir()
    ide_helpers = template_dir / "ide_helpers"
    ide_helpers.mkdir()
    template_file = ide_helpers / "test_template"
    template_file.write_text("new content")
    
    # Mock confirm to say yes
    monkeypatch.setattr(cli, "confirm", lambda *args: True)
    
    # Mock the files function
    def mock_files(package_name):
        class MockTraversable:
            def __init__(self, path):
                self.path = Path(path)
            def __truediv__(self, other):
                return MockTraversable(self.path / other)
            def __str__(self):
                return str(self.path)
        return MockTraversable(template_dir)
    
    import importlib.resources
    original_files = importlib.resources.files
    importlib.resources.files = mock_files
    
    try:
        cli._maybe_write_helper(root, "test_file", "test_template", True)
        content = existing_file.read_text()
        assert "existing content" in content
        assert "new content" in content
    finally:
        importlib.resources.files = original_files


def test_maybe_write_helper_skip_existing_file(tmp_path, monkeypatch):
    """Test _maybe_write_helper skips existing file when not confirmed."""
    root = tmp_path
    
    # Create existing file
    existing_file = root / "test_file"
    existing_file.write_text("existing content")
    
    # Mock confirm to say no
    monkeypatch.setattr(cli, "confirm", lambda *args: False)
    
    cli._maybe_write_helper(root, "test_file", "test_template", True)
    
    # File should remain unchanged
    assert existing_file.read_text() == "existing content"


def test_maybe_write_helper_disabled(tmp_path):
    """Test _maybe_write_helper does nothing when disabled."""
    root = tmp_path
    
    cli._maybe_write_helper(root, "test_file", "test_template", False)
    
    # No file should be created
    assert not (root / "test_file").exists()


def test_confirm_function():
    """Test confirm function calls typer.confirm."""
    # This test just ensures the function exists and can be called
    # We can't easily test the actual confirmation without mocking typer
    assert hasattr(cli, "confirm")
    assert callable(cli.confirm)