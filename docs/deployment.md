# Deployment Guide

This project includes two helper scripts. `bootstrap.sh` can be run on a Debian or Ubuntu system to clone the repository and run the installer automatically.
`install.sh` lives inside the repository and sets up dependencies and the
systemd service.

## Step-by-step guide

1. **Install Debian or Ubuntu (e.g., Raspberry Pi OS Lite or Ubuntu 22.04)** using your preferred imaging tool. Enable SSH so the
   Pi can be accessed over the network.
2. **Log in and download the bootstrap installer**:

   ```bash
   curl -L https://github.com/wagskydive/ai-telephone/raw/main/bootstrap.sh \
       -o bootstrap.sh
   sudo bash bootstrap.sh
   ```

   This script installs `git`, clones the repository to `/opt/ai-telephone` and
   then runs `install.sh` from that directory. `install.sh` creates the Python
   virtual environment, installs dependencies and registers the
   `ai-telephone.service` unit.
3. **Start the service**:

   ```bash
   sudo systemctl start ai-telephone.service
   ```

After these steps the backend API will run automatically on boot.
Check the service status with `sudo systemctl status ai-telephone.service`. Logs
can be viewed using `journalctl -u ai-telephone.service`.

If your TTS server runs remotely, set the `CHATTERBOX_URL` environment variable
in `/etc/environment` and reboot so the service picks it up.
