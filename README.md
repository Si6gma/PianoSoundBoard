<!--
Suggested GitHub Topics:
- python
- midi
- pygame
- soundboard
- music
- hobby-project
- audio
-->

# PianoSoundBoard

A Python-based MIDI soundboard that transforms a digital piano into a meme sound effect trigger pad.

## What It Is

PianoSoundBoard is a fun hobby project that maps MIDI keyboard notes to play custom audio files (meme sound effects). When you press specific keys on a MIDI-connected digital piano, it triggers sounds like "bruh", "rickroll", "roblox death sound", and more.

## Why It Exists

This project was created as a creative experiment to combine music hardware with internet culture. It demonstrates real-time MIDI input handling and audio playback, turning a traditional piano into an interactive soundboard for entertainment.

## Tech Stack

- **Python 3** - Core language
- **mido** - MIDI message handling and device communication
- **pygame** - Audio playback (mixer module)

## Prerequisites

```bash
pip install mido pygame
```

**Hardware Required:** A MIDI-capable digital keyboard connected to your computer.

## How to Run

1. Connect your digital piano via USB-MIDI
2. Find your device name:
   ```bash
   python device_name.py
   ```
3. Update `input.py` with your device name (if different from 'Digital Keyboard')
4. Run the soundboard:
   ```bash
   python input.py
   ```
5. Play the mapped keys on your piano to trigger sounds!

### Current Key Mappings

| MIDI Note | Sound Effect |
|-----------|--------------|
| 60 (C4)   | connect.mp3  |
| 62 (D4)   | trollface.mp3|
| 64 (E4)   | disconnect.mp3|
| 65 (F4)   | roblox.mp3   |
| 67 (G4)   | rickroll.mp3 |
| 69 (A4)   | bruh.mp3     |

## Project Structure

```
PianoSoundBoard/
├── Audio/              # Sound effect files (.mp3)
│   ├── bruh.mp3
│   ├── connect.mp3
│   ├── disconnect.mp3
│   ├── rickroll.mp3
│   ├── roblox.mp3
│   └── trollface.mp3
├── device_name.py      # Utility to list MIDI input devices
├── input.py            # Main application - MIDI listener & sound player
├── .gitignore          # Python gitignore
├── LICENSE             # MIT License
└── README.md           # This file
```

## Key Learnings

- **Real-time MIDI Integration:** Learned how to capture and process MIDI events in real-time using the `mido` library, handling note on/off events with velocity detection.

- **Audio Management:** Used `pygame.mixer` for non-blocking audio playback, enabling polyphonic-like behavior where sounds can overlap.

- **Hardware Abstraction:** Built a simple mapping system that decouples hardware input (MIDI notes) from application logic, making it easy to remap sounds.

- **Device Discovery:** Implemented MIDI device enumeration to handle different hardware configurations across systems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Built as a fun weekend project exploring Python audio and MIDI capabilities.*
