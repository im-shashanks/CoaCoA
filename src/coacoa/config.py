from pathlib import Path
import yaml
from typing import Any, Dict, Optional

def load_config(project_root: Path) -> Dict[str, Any]:
    base = project_root / ".coacoa" / "coacoa.yaml"
    cfg: Dict[str, Any] = yaml.safe_load(base.read_text())  # required
    override = project_root / "coacoa.yaml"
    if override.exists():
        ov = yaml.safe_load(override.read_text()) or {}
        cfg = _deep_merge(cfg, ov)
    return cfg

def _deep_merge(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and k in a:
            a[k] = _deep_merge(a[k], v)
        else:
            a[k] = v
    return a

def detect_venv(root: Path) -> Optional[Path]:
    for name in (".venv", ".env"):
        cand = root / name
        if (cand / "bin" / "python").exists():
            return cand
    # Poetry: top-level .venv sibling
    if (root.parent / ".venv" / "bin" / "python").exists():
        return root.parent / ".venv"
    return None