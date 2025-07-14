# Chatterbox TTS Integration Plan – AI Telephone

This document outlines how to integrate [Chatterbox TTS](https://github.com/chatterboxtts/chatterbox) as a fast, local text-to-speech backend alongside an Ollama-hosted LLM on a Vast.ai cloud server.

---

## 🧱 Architecture

### Vast.ai Server Stack

| Component     | Tool         | Role                       |
|---------------|--------------|----------------------------|
| LLM           | Ollama       | Generates responses        |
| TTS           | Chatterbox   | Converts LLM reply to WAV  |
| API Server    | Flask        | Hosts `/process-text` and `/process-audio` endpoints |

---

## 🔧 Chatterbox Installation (on Vast.ai)

```bash
sudo apt update && sudo apt install -y ffmpeg python3-pip
git clone https://github.com/chatterboxtts/chatterbox.git
cd chatterbox
pip3 install -r requirements.txt
python3 app.py --device cpu  # or use CUDA if GPU present
```

Once running, Chatterbox TTS will be accessible at:

```
http://<vast-server-ip>:7860/speak
```

---

## 📡 Integration in API Server

### `tts.py` (new or modified)
```python
import requests

def synthesize(text: str) -> bytes:
    response = requests.post(
        "http://<vast-server-ip>:7860/speak",
        json={"text": text}
    )
    response.raise_for_status()
    return response.content  # binary WAV audio
```

---

## 🧪 API Call Lifecycle (With Chatterbox)

1. Pi records audio and runs Whisper locally ✅
2. Transcribed text + prompt sent to `/process-text` on the Vast.ai server
3. Flask app:
   - Builds full prompt
   - Sends it to Ollama (`generate_response`)
   - Sends LLM reply text to Chatterbox (`synthesize`)
4. Returns TTS WAV back to Pi
5. Pi plays WAV via `aplay`

---

## 🔄 Endpoint Example: `/process-text`

```python
@app.post("/process-text")
def process_text():
    check_key()
    data = request.json
    text = data["text"]
    prompt = data["prompt"]
    reply = generate_response(text, prompt)
    wav = synthesize(reply)
    return send_file(io.BytesIO(wav), mimetype="audio/wav")
```

---

## ✅ Benefits

- Fast, locally hosted TTS with good voice quality
- Avoids cloud latency and API limits (e.g., ElevenLabs)
- Easy to switch voices and models

---

## 🧩 Next Steps

- [ ] Deploy Chatterbox on your Vast.ai Ollama server
- [ ] Update `tts.py` in your Flask backend
- [ ] Add fallback handling if Chatterbox is offline
- [ ] Test TTS latency and tune voice settings
