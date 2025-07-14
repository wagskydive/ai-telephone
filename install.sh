#!/bin/bash
set -e

# Simple installation helper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo cp systemd/ai-telephone.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ai-telephone.service
