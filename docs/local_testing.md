# Local Audio Testing

Use `simulate_call.py` to run the speech pipeline without phones or Asterisk. This helps verify your STT, LLM and TTS setup locally.

```bash
python -m src.simulate_call --text "Hello" --tts dummy --out reply.wav
```

You can also pass a WAV file recorded elsewhere:

```bash
python -m src.simulate_call --audio input.wav --tts espeak
```

The resulting audio is saved to `reply.wav` and played automatically.
