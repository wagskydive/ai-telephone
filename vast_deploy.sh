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

nohup python -m src.api_server &
