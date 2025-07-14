from pathlib import Path

from src.memory_logger import log_interaction, load_memory, summarize_memory


def test_log_and_load(tmp_path):
    memory_dir = tmp_path / "mem"
    log_interaction(memory_dir, "captain", caller_extension="600", summary="hi", name_guess="Bob", quotes=["hello"])
    log_interaction(memory_dir, "captain", caller_extension="601", summary="bye", name_guess="Ann", quotes=[])

    data = load_memory(memory_dir, "captain")
    assert len(data) == 2
    assert data[0]["caller_extension"] == "600"
    assert data[1]["summary"] == "bye"
    assert summarize_memory(data) == "hi; bye"
    # limit should restrict entries
    assert summarize_memory(data, limit=1) == "bye"


def test_log_pruning(tmp_path):
    memory_dir = tmp_path / "mem"
    for i in range(5):
        log_interaction(
            memory_dir,
            "p",
            caller_extension=str(i),
            summary=str(i),
            name_guess="",
            quotes=[],
            max_entries=3,
        )

    data = load_memory(memory_dir, "p")
    # Should keep only last three entries
    assert [d["summary"] for d in data] == ["2", "3", "4"]
