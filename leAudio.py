import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Define the path to your audio file
audio_file_path = 'mikejebait-3.mp3'

# Load your song 
pygame.mixer.music.load(audio_file_path)

# Play it
pygame.mixer.music.play()

# Keep the program running until the music is done
while pygame.mixer.music.get_busy():
    # You can add a short delay to reduce CPU usage
    time.sleep(0.1)
