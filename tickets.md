# Project Tickets

## T1 - Repository Skeleton Setup
- [x] Started
- [ ] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Initialize project directory structure (/src, /data, /docs, /lib) and move design and planning docs into /docs.

## T2 - Basic Voice Interface
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Implement initial voice interface with VAD recording, WAV playback, and call handling hooks.

## T3 - Character System Basics
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Define personalities.json schema, load personalities, map extensions 701-705, and handle random personality for extension 1000.

## T4 - Memory Logger Integration
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Implement memory_logger.py to save per-character interaction logs and call it from call_handler.

## T5 - Situation Engine
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add situation_generator module and integrate it with call_handler to request call context from the LLM server.

## T6 - Backend API Server
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Implement Flask backend API with `/process-audio` and `/generate-situation` endpoints.

## T7 - Raspberry Pi & Asterisk Setup
- [x] Started
- [ ] Tests Written
- [ ] Code Written
- [ ] Tests Passed
- [x] Documentation Written

Description: Install Raspberry Pi OS Lite, set up Asterisk with ATA and mini PBX, and verify trunk dial-out.

## T8 - Whisper and TTS Integration
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add Whisper transcription and text-to-speech support to the voice interface and processing server.

## T9 - Character Card Generation
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Generate printable character cards from personalities.json for players.

## T10 - Initiative-Based Outbound Calls
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Implement an outbound call loop that selects characters based on their initiative score.

## T11 - Prompt Design and Greeting Logic
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Finalize prompt format and use the LLM to inject greeting mood and situations at call start.

## T12a - API Key Security
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Require an ``X-API-Key`` header for API calls when configured.

## T12 - Backend Pipeline and Security Enhancements
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add Whisper and LLM pipeline, provide multiple TTS options, and secure the API endpoints for Raspberry Pi use.

## T13 - Deployment and Polishing
- [x] Started
- [ ] Tests Written
- [ ] Code Written
- [ ] Tests Passed
- [x] Documentation Written

Description: Create install script and systemd service, optimize TTS latency, finalize memory summarization, and perform final character recognition testing.

## T14 - LLM Integration Pipeline
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Implement actual LLM processing within `/process-audio` so transcribed text is sent to a language model and the response is synthesized.

## T15 - Enhanced TTS Options
- [x] Started
- [ ] Tests Written
- [ ] Code Written
- [ ] Tests Passed
- [ ] Documentation Written

Description: Add additional TTS backends (including ElevenLabs) and expose a user-selectable option in the GUI.
