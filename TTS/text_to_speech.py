from gtts import gTTS
import os

text = open("input_text.txt", "r").read().replace("\n", " ") # Open file, store tokens into text variable
language = 'en' # TODO: How do we make it automatically recognize other languages?

tts = gTTS(text)
tts.save('speech.wav') # Save our text into a .wav file which is automatically saved to your Colab session storage
sound_file = 'speech.wav'
Audio(sound_file, autoplay = True) # Play automatically, look into alternatives
