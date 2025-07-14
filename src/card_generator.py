"""Generate simple character cards from personalities."""
from __future__ import annotations

from pathlib import Path

from .personalities import load_personalities


def generate_cards(personality_file: Path, output_dir: Path) -> None:
    """Create a text card file for each personality."""
    personalities = load_personalities(personality_file)
    output_dir.mkdir(parents=True, exist_ok=True)
    for p in personalities:
        card = output_dir / f"{p.id}.txt"
        card.write_text(f"{p.name} ({p.extension})\n{p.tagline}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate personality cards")
    parser.add_argument("personalities")
    parser.add_argument("output")
    args = parser.parse_args()

    generate_cards(Path(args.personalities), Path(args.output))
