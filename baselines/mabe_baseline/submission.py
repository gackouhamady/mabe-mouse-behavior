from pathlib import Path
import pandas as pd
from typing import Optional, Iterable

REQUIRED_COLS = ["row_id","video_id","agent_id","target_id","action","start_frame","stop_frame"]

def header_only_submission(path: Path) -> None:
    pd.DataFrame(columns=REQUIRED_COLS).to_csv(path, index=False)

def normalized_submission(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure columns exist & correct order
    for c in REQUIRED_COLS:
        if c not in df.columns:
            df[c] = []  # create missing
    return df[REQUIRED_COLS]

def from_sample(sample_csv: Path, out_csv: Path) -> None:
    sample = pd.read_csv(sample_csv)
    # If the sample already has the right schema and rows, just keep it (baseline).
    df = normalized_submission(sample)
    df.to_csv(out_csv, index=False)

def write_dummy_events(video_ids: Iterable[str], out_csv: Path) -> None:
    # Produce one trivial "sniff" event per video (baseline sanity).
    rows = []
    rid = 0
    for vid in video_ids:
        rows.append([rid, str(vid), "mouse1", "mouse2", "sniff", 0, 10])
        rid += 1
    df = pd.DataFrame(rows, columns=REQUIRED_COLS)
    df.to_csv(out_csv, index=False)
