from pathlib import Path
from src.analytics import compute_stats
import json

def test_compute_stats(tmp_path: Path):
    mem = tmp_path / "memory"
    mem.mkdir()
    (mem / "a.json").write_text(json.dumps([{"caller_extension": "1"}, {}]))
    (mem / "b.json").write_text(json.dumps([{}]))
    stats = compute_stats(mem)
    assert stats["totals"] == {"a": 2, "b": 1}
    assert stats["most_popular"] == "a"
