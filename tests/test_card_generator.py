from pathlib import Path

from src.card_generator import generate_cards
from src.personalities import Personality


def test_generate_cards(tmp_path):
    data = [
        {
            "id": "a",
            "name": "A",
            "extension": 701,
            "initiative": 0.1,
            "tagline": "t",
            "prompt": "p",
        }
    ]
    pfile = tmp_path / "p.json"
    pfile.write_text(__import__("json").dumps(data))
    outdir = tmp_path / "cards"
    generate_cards(pfile, outdir)
    card = outdir / "a.txt"
    assert card.exists()
    assert "A" in card.read_text()
