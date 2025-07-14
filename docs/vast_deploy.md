# Vast.ai Deployment

`vast_deploy.sh` automates setting up the backend API on a Vast.ai instance.
The script installs system packages, clones this repository and starts the API
server inside a Python virtual environment.

Run it on a fresh Ubuntu image:

```bash
bash vast_deploy.sh
```

After execution, the Flask server will be running in the background on
port 5000.  The script also clones and launches Chatterbox TTS so that the API
can use fast local speech synthesis.  By default the Chatterbox server listens
on port 7860 and the API is started with ``CHATTERBOX_URL`` pointing at this
local instance.
