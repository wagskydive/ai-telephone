#!/bin/bash
set -e

# Installation script for a fresh Raspberry Pi.

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

apt-get update
apt-get install -y git python3 python3-venv asterisk

if [ ! -d /opt/ai-telephone ]; then
    git clone https://github.com/wagskydive/ai-telephone.git /opt/ai-telephone
fi

cd /opt/ai-telephone
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp systemd/ai-telephone.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable ai-telephone.service
