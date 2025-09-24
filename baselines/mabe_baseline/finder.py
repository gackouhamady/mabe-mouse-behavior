from pathlib import Path
from typing import Optional

def find_competition_root() -> Optional[Path]:
    root = Path("/kaggle/input")
    if not root.exists():
        return None
    # Prefer exact slug if present
    for p in root.iterdir():
        name = p.name.lower()
        if "mabe" in name and "mouse" in name and p.is_dir():
            return p
    # Fallback: first directory
    for p in root.iterdir():
        if p.is_dir():
            return p
    return None

def find_sample_submission(comp_root: Path) -> Optional[Path]:
    if comp_root is None:
        return None
    cand = comp_root / "sample_submission.csv"
    return cand if cand.exists() else None
