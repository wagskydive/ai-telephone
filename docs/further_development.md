# Further Development Checklist – AI Telephone

This document outlines prioritized enhancements and cleanup tasks to improve and extend the AI Telephone system.

---

## 🥇 High Priority

- [ ] ✅ Add fallback handling for Whisper/LLM/TTS failure
- [ ] ✅ Implement `/generate-situation` endpoint server-side using `situation_generator.py`
- [ ] ✅ Add `/process-text` endpoint to support Pi-side Whisper and text-only input
- [ ] ✅ Wrap `record_until_silence()` and LLM requests in `try/except` with logging
- [ ] ✅ Add periodic `run_outbound()` loop for autonomous character calls
- [ ] ✅ Improve logging throughout (`call_handler.py`, `api_server.py`)

---

## 🥈 Medium Priority

- [ ] 🔄 Add history check to prevent characters calling same extension too often
- [ ] 🔄 Add ability to pause or disable individual personalities from calling
- [ ] 🔄 Expand `log_interaction()` to prune after N entries or rotate logs
- [ ] 🔄 Add inferred name guessing logic to prompt/summary pipeline
- [ ] 🔄 Improve error handling in API server (e.g. malformed audio, missing fields)

---

## 🥉 Optional / Bonus Features

- [ ] 🧩 Create a web-based GUI (Flask or React) for:
  - Editing characters, extensions, initiative values
  - Live logs and system status
  - TTS/VAD test tools

- [ ] 🖨️ Implement `card_generator.py` to generate printable PDFs for each AI character

- [ ] 🌍 Create Vast.ai deployment shell script:
  - GPU setup
  - Install Ollama + Python
  - Deploy `api_server.py` + models

- [ ] 📊 Build analytics dashboard (calls/hour, most popular character, etc.)

- [ ] 🔉 Add local audio testing CLI (`simulate_call.py`)

---

## 🧪 Final Testing Suggestions

- [ ] Confirm Pi-side VAD triggers reliably
- [ ] Test with >1 character in outbound mode
- [ ] Log name recognition + reuse across multiple calls
- [ ] Simulate flaky network to ensure LLM timeouts are caught

