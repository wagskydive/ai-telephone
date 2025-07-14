# AI Telephone System – Technical Design Document

## Overview
This project connects vintage analog telephones to AI personalities via a Raspberry Pi running Asterisk and a locally hosted or remote Ollama LLM server. When a user picks up a phone or receives a call, they interact with one of many dynamic, humorous skydiving-themed AI characters. All interaction is natural (voice-only), with voice activity detection (VAD), local transcription via Whisper, and speech synthesis.

## Key Features
- Natural-mode AI conversation over analog telephony
- Skydiving-themed AI personalities with memory
- Random character assignment + personal extensions
- Fully offline-capable using Whisper + Ollama
- Situational awareness with LLM-generated dynamic prompts
- Web-based GUI for managing personalities and settings

## Hardware Architecture
- **Phones**: Up to 8 analog phones connected to a mini PBX
- **Mini PBX**: Routes internal calls and trunk line
- **ATA**: 2-port Analog Telephone Adapter (e.g., HT802)
- **Raspberry Pi**: Runs Asterisk + AI bridge logic + local GUI
- **Ethernet**: Networked to Ollama server or internet

## Software Components
### Asterisk PBX (on Pi)
- Receives calls via SIP from ATA
- Routes calls to Python scripts
- Dialplan extensions:
  - `701-705`: Direct line to characters
  - `1000`: Random character

### Python Services
- **call_handler.py**
  - Manages VAD recording loop
  - Sends audio to LLM backend
  - Receives and plays AI response
- **vad_recorder.py**
  - Uses `sounddevice` and `webrtcvad` to capture speech
- **audio_player.py**
  - Plays WAV responses via the system `aplay` command

- **memory_logger.py**
  - Maintains a per-character JSON log in ``memory/``
  - Summarizes conversations
  - Extracts caller name if spoken

- **situation_generator.py**
  - Prompts LLM to generate a “current situation”
  - Adds realism/mood to the character's response
- **prompt_builder.py**
  - Combines the personality prompt, memory snippets and situation
    into a final prompt sent to the LLM

- **Flask GUI App (gui/app.py)**
  - Web server running on the Pi
  - Shows system settings and character list
  - Allows editing extensions, LLM URLs, initiative values, etc.
  - Live memory viewer and test tools (VAD, TTS)

### LLM Server (Ollama or OpenAI)
- **/process-audio**
  - `POST`
  - Request: `{ audio_file (binary), character_id (string), caller_extension (string), prompt (string?) }`
  - Header `X-API-Key` required when the server is started with an API key
  - Process: Whisper STT → Build prompt → LLM response → TTS → WAV
  - Response: WAV audio (binary)

- **/generate-situation**
  - `POST`
  - Request: `{ character_id (string), memory_snippets (list of strings), personality_prompt (string) }`
  - Process: LLM generates realistic or comical phone-answering scenario
  - Response: `{ situation: string }`

- **/log-memory** *(optional)*
  - `POST`
  - Request: `{ character_id, caller_extension, name_guess, summary, quotes }`
  - Stores interaction to persistent character memory log
  
These endpoints are implemented in the small Flask server provided by
``src.api_server.create_app``.

## Personality Design
- Characters defined in `data/personalities.json` and loaded by ``src.personalities``:
```json
{
  "id": "captain_freefall",
  "name": "Captain Freefall",
  "extension": 701,
  "initiative": 0.9,
  "tagline": "Yell something and brace for chaos.",
  "prompt": "Your name is Captain Freefall. You're a fearless, loud, overly confident ex-military skydiver..."
}
```
- Initiative value determines chance of initiating outbound calls

## Memory Format
- One file per character (e.g. `memory/captain_freefall.json`)
- Appends each user interaction:
```json
{
  "timestamp": "2025-07-13T15:42:22Z",
  "caller_extension": "601",
  "name_guess": "Luke",
  "summary": "Luke asked about fear. Freefall told him to yell.",
  "quotes": ["Yelling builds speed!"]
}
```

## Prompt Protocol
- Injects:
  - Personality prompt
  - Last 2–3 memory summaries
  - Current LLM-generated situation
  - Role: “You are on a phone call. Speak accordingly.”

## AI Call Loop
- Periodic script chooses characters based on `initiative`
- Picks random extensions to call
- Uses `channel originate` to trigger AI-call flow

## Audio Pipeline
1. Phone → Asterisk (SIP trunk via ATA)
2. Asterisk → `call_handler.py`
3. Python records with VAD
4. Audio sent to `/process-audio`
5. Whisper → LLM → TTS (supports `espeak`, `pyttsx3`, and an optional ElevenLabs backend selectable via the GUI)
6. WAV sent back → played via `aplay`

## GUI Settings Panel
- Runs locally on the Raspberry Pi (Flask)
- Accessible via browser (e.g. `http://raspberrypi.local:8080`)
- Key pages:
  - Dashboard (active calls, LLM status)
  - Edit Personalities (initiative, extension, prompt)
  - Audio Tools (test TTS, test VAD mic)
  - Logs (view memory summaries)

## Print Materials
- Each character gets a printed card:
  - Name, extension, tagline
  - Call instructions
- Stored in `personalities.json` for PDF/PNG generation
