# Run Program: python -m speech_recognition
import speech_recognition as sr
import pyttsx3

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

        web.get(path).open(MyText)

    else:
        MyText = MyText.lower()

        print("Did you say " +MyText)
        SpeakText(MyText)