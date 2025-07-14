# Deployment Guide

This project includes a helper script `install.sh` which sets up a Python virtual environment, installs dependencies and installs a systemd service file `ai-telephone.service`.

To install on a Raspberry Pi:

```bash
./install.sh
sudo systemctl start ai-telephone.service
```

The service will start the backend API on boot.
