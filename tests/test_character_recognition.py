import json
from pathlib import Path


def test_prompts_include_name():
    path = Path('data/personalities.json')
    data = json.loads(path.read_text())
    for entry in data:
        name = entry['name']
        assert name in entry['prompt']
