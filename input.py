import mido
import pygame
import time

# Open your MIDI device
inport = mido.open_input('Digital Keyboard')
pygame.mixer.init()

# # Create a dictionary mapping note numbers to audio files
note_to_audio = {
    60: 'connect.mp3',
    62: 'trollface.mp3',
    64: 'disconnect.mp3'
}

# Listen for messages from the MIDI device
for msg in inport:
    # If the message is a note on message and the velocity is greater than 0
    if msg.type == 'note_on' and msg.velocity > 0:
        print('Note on:', msg.note)
        # If the note is in the dictionary, play the corresponding audio file
        if msg.note in note_to_audio:
            audio_file_path = note_to_audio[msg.note]
            pygame.mixer.music.load(audio_file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
