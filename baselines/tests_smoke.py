from pathlib import Path
import pandas as pd
from mabe_baseline.submission import REQUIRED_COLS, header_only_submission, normalized_submission

def test_header_only(tmp_path: Path):
    out = tmp_path / "sub.csv"
    header_only_submission(out)
    df = pd.read_csv(out)
    assert list(df.columns)==REQUIRED_COLS
    assert df.empty

def test_normalized_submission():
    df = pd.DataFrame({"row_id":[0],"video_id":["v1"],"action":["sniff"],
                       "agent_id":["mouse1"],"target_id":["mouse2"],
                       "start_frame":[0],"stop_frame":[5]})
    df2 = normalized_submission(df)
    assert list(df2.columns)==REQUIRED_COLS
