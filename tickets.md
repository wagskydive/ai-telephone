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
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
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
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add additional TTS backends (including ElevenLabs) and expose a user-selectable option in the GUI.

## T16 - Create install script that downloads the repo and makes it work on a clean Raspberry Pi installation
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: We need to be able to clone the repo and run one script that installs everything. Plus a guide that explains the full install guide flashing a fresh raspberry pi install to cloning the repo and running the install script. The explaination should be understandable for anyone without any knowledge.

## T17 - Write a cmplete user manual
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: We need an operation manual that explains the workings of the app


## T16 - TTS Latency Optimization
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Profile and reduce audio playback latency, ensuring snappy responses on the Pi.


## T18 - Character Recognition Testing
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Validate that each AI personality consistently identifies themselves during conversations.

## T19 - Bootstrap Installer
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add bootstrap.sh that installs git, clones the repo and executes install.sh for one-command installation.

## T20 - Project README
- [x] Started
- [ ] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Create a standard README with overview, installation and usage instructions.

## T21 - Chatterbox Integration
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add Chatterbox TTS backend with fallback handling.

## T22 - Further Development Tasks
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Begin implementing items listed in further_development.md.

## T23 - Outbound Call History Check
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Prevent characters from repeatedly calling the same extension by keeping a short call history and skipping recently dialed numbers.
## T24 - Voice Pipeline Fallback Handling
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add fallback handling when Whisper, LLM, or TTS components fail so calls continue gracefully.

## T25 - Process Text Endpoint
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add `/process-text` endpoint to the API server to support Pi-side Whisper and text-only input.

## T26 - Robust Recording and LLM Requests
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Wrap `record_until_silence()` and LLM requests in `try/except` blocks with proper logging.

## T27 - Improved Logging
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Increase logging detail in `call_handler.py` and `api_server.py` for easier debugging.

## T28 - Personality Pause/Disable
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add ability to pause or disable individual personalities from making outbound calls.

## T29 - Log Pruning
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Expand `log_interaction()` to prune logs after a set number of entries or rotate log files.

## T30 - Name Guessing Logic
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Add inferred name guessing in the prompt and summary pipeline to personalize interactions.

## T31 - API Error Handling Improvements
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Improve error handling in the API server for malformed audio or missing fields.

## T32 - Web-Based GUI
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
 - [x] Documentation Written

Description: Build a web-based GUI for editing characters, viewing live logs, and running TTS/VAD tests.

## T33 - Vast.ai Deployment Script
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
 - [x] Documentation Written

Description: Create a shell script to deploy the backend on Vast.ai including GPU setup and model installation.

## T34 - Analytics Dashboard
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Implement a dashboard showing call statistics such as calls per hour and most popular characters.

## T35 - Local Audio Testing CLI
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Provide a command-line tool (`simulate_call.py`) to test audio processing locally.

## T36 - VAD Reliability Testing
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Confirm that Pi-side voice activity detection reliably triggers recording.

## T37 - Multi-Character Outbound Test
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Test outbound calling with more than one character active at a time.

## T38 - Name Recognition Persistence
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
 - [x] Documentation Written

Description: Log recognized names and reuse them across multiple calls for continuity.

## T39 - Network Failure Simulation
- [x] Started
- [x] Tests Written
- [x] Code Written
- [x] Tests Passed
- [x] Documentation Written

Description: Simulate flaky network conditions to ensure LLM timeouts and related errors are properly handled.

## T40 - Field-Ready Release Polish
- [ ] Started
- [ ] Tests Written
- [ ] Code Written
- [ ] Tests Passed
- [ ] Documentation Written

Description: Finalize documentation and cleanup for a field-ready release, ensuring installation steps and code examples are up to date.
