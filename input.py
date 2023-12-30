import mido
import pygame
import time

# Open your MIDI device
inport = mido.open_input('Digital Keyboard')
pygame.mixer.init()

# Create a dictionary mapping note numbers to audio files
note_to_audio = {
    60: pygame.mixer.Sound('Audio/connect.mp3'),
    62: pygame.mixer.Sound('Audio/trollface.mp3'),
    64: pygame.mixer.Sound('Audio/disconnect.mp3'),
    65: pygame.mixer.Sound('Audio/roblox.mp3'),
    67: pygame.mixer.Sound('Audio/rickroll.mp3')
}

# Listen for messages from the MIDI device
for msg in inport:
    # If the message is a note on message
    if msg.type == 'note_on':
        # If the velocity is greater than 0 (key press), play the corresponding audio file
        if msg.velocity > 0:
            print('Note on:', msg.note)
            if msg.note in note_to_audio:
                note_to_audio[msg.note].play()
        # If the velocity is 0 (key release), stop the audio
        else:
            if msg.note in note_to_audio:
                note_to_audio[msg.note].stop()
