# Main.py where we run our program, and keep control of all called processes.

import keyboard
# from TTC import ClosestCommand

if __name__ == "__main__":
    response = ""
    while True:
        if keyboard.is_pressed('ctrl+r'):
            print("listening")
            response = "run code"
            # Run Speech to Text
        elif response != "":
            print("Run TTC")
        else:
            print("Not listening")

