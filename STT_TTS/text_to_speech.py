from gtts import gTTS
import os
import pyttsx3
import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()
# Run Program: python -m speech_recognition
import speech_recognition as sr
import pyttsx3

#TODO: Use accessible_output2 to recognize if user has a screen reader, use their voice and rate first
# If not, use the default. Ask Thomas if he can help with this.

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

    # Path to Google Chrome
    path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

# Use the microphone as source for input
with sr.Microphone() as source2:

    # Wait for the recognizer to adjust the energy threshold based on the background noise
    r.adjust_for_ambient_noise(source2, duration=0.2)

    # Listens for the user's input
    audio2 = r.listen(source2)

    # Using google to recognize audio
    MyText = r.recognize_google(audio2)

    if MyText == "open website":
        print("You have said: " + MyText)
        print("What website would you like?")

        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)

    else:
        MyText = MyText.lower()

        print("Did you say " +MyText)
        SpeakText(MyText)

# Below code is the proof of concept
#sample_string = 'North Texas.'  # Sample string dataset

#speech_output_2 = gTTS(sample_string, lang = 'en', slow = True)
#speech_output_2.save("test_audio.mp3")
#os.system("test_audio.mp3")
#Audio("test_audio.mp3", autoplay=True)

# Once I receive the string from Solomon's STT, pass it into gTTS
print(MyText)
speech_output = gTTS(MyText, lang = 'en', slow = True)
speech_output.save("audio.mp3")
os.system("audio.mp3")
