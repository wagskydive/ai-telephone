# Deployment Guide

This project includes a helper script `install.sh` which can bootstrap a fresh
Raspberry Pi. The script installs required packages, clones this repository into
`/opt/ai-telephone` and installs a systemd service so the API starts on boot.

## Step-by-step guide

1. **Flash Raspberry Pi OS Lite** using Raspberry Pi Imager. Enable SSH so the
   Pi can be accessed over the network.
2. **Log in and download the installer**:

   ```bash
   curl -L https://github.com/wagskydive/ai-telephone/raw/main/install.sh \
       -o install.sh
   sudo bash install.sh
   ```

   The script will install `git`, `python3-venv` and `asterisk`, clone the
   repository to `/opt/ai-telephone`, create a virtual environment and register
   the `ai-telephone.service` systemd unit.
3. **Start the service**:

   ```bash
   sudo systemctl start ai-telephone.service
   ```

After these steps the backend API will run automatically on boot.
