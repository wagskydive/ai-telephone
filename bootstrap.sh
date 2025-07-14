#!/bin/bash
set -e

# Bootstrap installer for AI Telephone
# This script installs git, clones the repository and runs install.sh

REPO_DIR=/opt/ai-telephone
REPO_URL=https://github.com/wagskydive/ai-telephone.git

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

apt-get update
apt-get install -y git

if [ ! -d "$REPO_DIR" ]; then
    git clone "$REPO_URL" "$REPO_DIR"
else
    git -C "$REPO_DIR" pull
fi

cd "$REPO_DIR"
bash install.sh

