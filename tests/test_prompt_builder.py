from src.prompt_builder import build_prompt


def test_build_prompt():
    prompt = build_prompt("base", ["m1", "m2"], "s1")
    assert "base" in prompt
    assert "m1" in prompt and "m2" in prompt
    assert "s1" in prompt
