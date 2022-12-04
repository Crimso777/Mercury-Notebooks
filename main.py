# Main.py where we run our program, and keep control of all called processes.

import keyboard
from TTC import ClosestCommand
from Collaborator.colab import notebook

if __name__ == "__main__":
    # initiate Text to Commands class
    ttc = ClosestCommand.TextToCommands()
    nb = notebook("example")    # TODO: get notebook from user input
    
    response = ""
    while True:
        if keyboard.is_pressed('ctrl+r'):
            # While pressed, we are listening
            response = "run code"   # TODO: Add capture from solomon
            
            #match command
            command = ttc.findMatch(response)
            if command == None:
                # TODO: Error handling
                pass
            else:
                #find variable (if exists)
                variable = ttc.findVariables(response, command)
                
                #run command
                ttc.runCommand(nb, command, variable)
        else:
            # Wait for keyboard input
            pass
