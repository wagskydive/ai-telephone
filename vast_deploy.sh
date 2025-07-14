#!/bin/bash
# Deploy AI Telephone backend on a Vast.ai instance
set -e

REPO_URL=https://github.com/wagskydive/ai-telephone.git
DIR=ai-telephone

apt-get update
apt-get install -y git python3 python3-venv ffmpeg

if [ ! -d "$DIR" ]; then
    git clone "$REPO_URL" "$DIR"
else
    git -C "$DIR" pull
fi

cd "$DIR"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# install and launch Chatterbox TTS
if [ ! -d chatterbox ]; then
    git clone https://github.com/chatterboxtts/chatterbox.git
    pip install -r chatterbox/requirements.txt
fi
nohup python chatterbox/app.py --device cpu --port 7860 &

# start the API server after exporting the Chatterbox URL
export CHATTERBOX_URL=http://localhost:7860/speak
nohup python -m src.api_server &
