# Vast.ai Deployment

`vast_deploy.sh` automates setting up the backend API on a Vast.ai instance.
The script installs system packages, clones this repository and starts the API
server inside a Python virtual environment.

Run it on a fresh Ubuntu image:

```bash
bash vast_deploy.sh
```

After execution, the Flask server will be running in the background and serving
requests on port 5000.
