# Main.py where we run our program, and keep control of all called processes.

import keyboard
from TTC import ClosestCommand
from Collaborator.colab import notebook

if __name__ == "__main__":
    # initiate Text to Commands class
    ttc = ClosestCommand.TextToCommands()
    
    response = ""
    while True:
        if keyboard.is_pressed('ctrl+r'):
            print("listening")
            response = "run code"
            print(ttc.findMatch(response))
        elif response != "":
            print("Run TTC")
        else:
            print("Not listening")

