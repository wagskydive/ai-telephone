# AI Telephone System – Development Planning & Roadmap

## Overview
This planning document defines the phases and milestones to guide development of the AI-powered telephone system using analog phones, Asterisk, Raspberry Pi, and AI personality backends.

---

## Phase 1: Foundation Setup
**Goal:** Establish working Asterisk system and analog phone routing.

### Tasks:
- [ ] Install Raspberry Pi OS Lite
- [ ] Install Asterisk
- [ ] Configure ATA (2-port)
- [ ] Connect analog phones via mini PBX
- [ ] Confirm trunk dial-out works from Pi

---

## Phase 2: Voice Interface Layer
**Goal:** Create basic AI loop using VAD, Whisper, LLM, and TTS

### Tasks:
- [ ] `call_handler.py`: core handler script
- [ ] `vad_recorder.py`: record speech naturally
- [ ] `audio_player.py`: play WAV responses
- [ ] Add Whisper + TTS (local or remote)
- [ ] Create `/process-audio` endpoint (Flask or FastAPI)
- [ ] Test basic call → AI → response cycle

---

## Phase 3: Character System
**Goal:** Implement skydiving personalities with extensions and memory

### Tasks:
- [ ] Define character schema (`personalities.json`)
- [ ] Add unique extensions (701–705)
- [ ] Add random personality logic for ext 1000
- [ ] Print-ready character card generation
- [ ] Add initiative-based outbound call loop
- [ ] Integrate `memory_logger.py`
- [ ] Save memory log per character

---

## Phase 4: Situation Engine
**Goal:** Add LLM-generated call context and realism

### Tasks:
- [ ] Design prompt format
- [ ] Implement `situation_generator.py`
- [ ] Add call-start context logic to `call_handler.py`
- [ ] Use LLM to inject greeting mood/situation

---

## Phase 5: Backend API Server
**Goal:** Run all LLM interactions on local Ollama server

### Tasks:
- [ ] Flask app with:
  - `/process-audio` – main AI loop
  - `/generate-situation` – scene builder
- [ ] Add Whisper + LLM pipeline
- [ ] Add TTS return, give multiple options for TTS to user through gui, include Elevenlabs
- [ ] Secure endpoint for Pi use

---

## Phase 6: Deployment & Polish
**Goal:** Package and test final experience

### Tasks:
- [ ] Install all services via `install.sh`
- [ ] Add systemd service for startup
- [ ] Optimize TTS playback latency
- [ ] Final memory review logic (summarization tuning)
- [ ] Final test: character recognition by AI

---

## Milestones

| Milestone | Target Date       | Owner   | Status |
|----------|-------------------|---------|--------|
| Basic phone-to-AI call works | Week 1            | Lead Dev | 🔲     |
| Personalities + memory       | Week 2            | AI Dev   | 🔲     |
| Situation-aware characters   | Week 3            | Prompt Team | 🔲 |
| Fully autonomous call loop   | Week 4            | System Dev | 🔲 |
| Field-ready release          | Week 5            | Team     | 🔲     |
