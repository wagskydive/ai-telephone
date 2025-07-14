# User Manual

This manual explains how to operate the AI Telephone once it is installed.

## Making Calls
1. Pick up any connected analog phone.
2. Dial an extension between **701** and **705** to speak with a specific skydiving character.
3. Dial **1000** to be connected with a random character.
4. Speak naturally after the beep. Pause to let the AI respond.

## Receiving Calls
Characters may place calls automatically when the outbound call loop is running.
Simply pick up the ringing phone to answer.

## Adjusting Voices
Different text-to-speech backends can be selected in the web UI. Choose the
voice that sounds best for your setup.

## Viewing Memories
Each character keeps a log of conversations. Logs are stored in
`/opt/ai-telephone/memory` and can be opened with any text editor.

## Troubleshooting
- If no audio plays, ensure speakers or the handset are connected and `aplay`
  works from the command line.
- Restart the backend service with:
  ```bash
  sudo systemctl restart ai-telephone.service
  ```

For detailed setup instructions see the [Deployment Guide](deployment.md).
