from pathlib import Path

from src.personalities import load_personalities, get_by_extension, random_personality, select_personality


def test_load_and_select(tmp_path):
    data = [
        {"id": "a", "name": "A", "extension": 701, "initiative": 0.5, "tagline": "t", "prompt": "p"},
        {"id": "b", "name": "B", "extension": 702, "initiative": 0.3, "tagline": "t", "prompt": "p"},
    ]
    path = tmp_path / "p.json"
    path.write_text(__import__('json').dumps(data))

    personalities = load_personalities(path)
    assert get_by_extension(personalities, 701).id == "a"
    assert select_personality(personalities, 701).id == "a"
    # extension 1000 should return one of the personalities
    assert select_personality(personalities, 1000) in personalities
    # random function should return one of them
    assert random_personality(personalities) in personalities
