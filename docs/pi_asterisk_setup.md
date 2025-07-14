# Raspberry Pi & Asterisk Setup

This guide outlines how to prepare a Raspberry Pi or Ubuntu machine with Asterisk and connect analog phones through an ATA and mini PBX.

1. **Install Raspberry Pi OS Lite**
   - Flash the latest Lite image to an SD card using Raspberry Pi Imager.
   - Enable SSH and boot the Pi.

2. **Install Asterisk**
   - Update package lists: `sudo apt update`.
   - Install Asterisk and common dependencies:
     ```bash
     sudo apt install asterisk asterisk-dahdi
     ```

3. **Configure the ATA**
   - Connect the ATA to your network and mini PBX.
   - Use the web interface to configure two SIP accounts pointing at the Pi.

4. **Define Dialplan**
   - Edit `/etc/asterisk/extensions.conf` and add the extensions from `personalities.json` (701–705 and 1000).
   - Reload Asterisk: `sudo asterisk -rx 'dialplan reload'`.

5. **Verify Trunk Dial‑Out**
   - Pick up a phone and dial another extension.
   - The call should route through the ATA and reach the Pi.

This configuration is sufficient for local testing and matches the initial foundation described in the design document.
