# Further Development Checklist – AI Telephone

This document outlines prioritized enhancements and cleanup tasks to improve and extend the AI Telephone system.

---

## 🥇 High Priority

- [x] ✅ Add fallback handling for Whisper/LLM/TTS failure
- [x] ✅ Implement `/generate-situation` endpoint server-side using `situation_generator.py`
- [x] ✅ Add `/process-text` endpoint to support Pi-side Whisper and text-only input
- [x] ✅ Wrap `record_until_silence()` and LLM requests in `try/except` with logging
- [x] ✅ Add periodic `run_outbound()` loop for autonomous character calls
- [x] ✅ Improve logging throughout (`call_handler.py`, `api_server.py`)

---

## 🥈 Medium Priority

- [x] 🔄 Add history check to prevent characters calling same extension too often
- [x] 🔄 Add ability to pause or disable individual personalities from calling
- [x] 🔄 Expand `log_interaction()` to prune after N entries or rotate logs
- [x] 🔄 Add inferred name guessing logic to prompt/summary pipeline
- [x] 🔄 Improve error handling in API server (e.g. malformed audio, missing fields)

---

## 🥉 Optional / Bonus Features

 - [x] 🧩 Create a web-based GUI (Flask or React) for:
  - Editing characters, extensions, initiative values
  - Live logs and system status
  - TTS/VAD test tools

- [ ] 🖨️ Implement `card_generator.py` to generate printable PDFs for each AI character

 - [x] 🌍 Create Vast.ai deployment shell script:
  - GPU setup
  - Install Ollama + Python
  - Deploy `api_server.py` + models

- [ ] 📊 Build analytics dashboard (calls/hour, most popular character, etc.)

- [x] 🔉 Add local audio testing CLI (`simulate_call.py`)

---

## 🧪 Final Testing Suggestions

 - [x] Confirm Pi-side VAD triggers reliably
 - [x] Test with >1 character in outbound mode
 - [x] Log name recognition + reuse across multiple calls
- [ ] Simulate flaky network to ensure LLM timeouts are caught

