from pathlib import Path
import shutil, yaml
from coacoa.config import load_config, detect_venv

def test_deep_merge(tmp_path: Path):
    base = tmp_path / ".coacoa"
    base.mkdir()
    (base / "coacoa.yaml").write_text("a:\n  b: 1\n")
    override = tmp_path / "coacoa.yaml"
    override.write_text("a:\n  c: 2\n")

    cfg = load_config(tmp_path)
    assert cfg["a"] == {"b": 1, "c": 2}

def test_detect_venv(tmp_path: Path):
    assert detect_venv(tmp_path) is None
    venv = tmp_path / ".venv" / "bin"
    venv.mkdir(parents=True)
    (venv / "python").touch()
    assert detect_venv(tmp_path).name == ".venv"

def test_detect_venv_none(tmp_path: Path):
    assert detect_venv(tmp_path) is None