#from IPython.display import HTML, Audio
#from scipy.io.wavfile import read as wav_read
import speech_recognition as sr
import pyttsx3
import ffmpeg
#import io

# Recognizer instance which will recognize our speech via speech_recognition python library
r = sr.Recognizer()

def STT(speech):  
    # Create object
    engine = pyttsx3.init()
    engine.say(speech) 
    engine.runAndWait()
    
    # Speaking rate of the engine
    # TODO: Understand and modify speech rate property accordingly
    # speech_rate = engine.getProperty('rate')
    # print (speech_rate)

    # Modify volume
    # TODO: Understand and modify volume property accordingly
    # speech_volume = engine.getProperty('volume')
    # print (speech_volume)   

    # Modify voice
    # TODO: Understand and modify voice roperty accordingly
    # voices = engine.getProperty('voices')
   
    # Save the speech to an mp3 file which can be read back to speech
    # TODO: Look into .wav
    engine.save_to_file('Speech to Text Test', 'testing.mp3')
    engine.runAndWait()

# Listen to speech indefinitely
while(1):    
    # Handle exceptions at runtime
    try:
        # Assume user is using microphone on their device
        with sr.Microphone() as user_speech:
              
            # Sr recognizer must briefly wait to adjust to any outside interference on microphone
            r.adjust_for_ambient_noise(user_speech, duration = 1)
              
            # Listen to speech input on microphone 
            playback = r.listen(user_speech)
              
            # Utilizing Google's API to recognize the spoken words
            text_output = r.recognize_google(playback)
            text_output = text_output.lower()
  
            # Play back audio of user_speech
            STT(text_output)
            print("(test) User's spoken input is : ", text_output) 
              
    except sr.UnknownValueError:
        print("Error: Unknown input")
