'''
THIS SOFTWARE IS JUST FOR WINDOWS, Because of the python-setup-file.bat on line 30. change it so that it will compatible with another os

and this software is made from a hard way too. theres a easier way but i didnt use it
'''
import os
import json,subprocess,colorama

current_dir, main_dir = os.path.dirname(os.path.abspath(__file__)), os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(main_dir + "/python-setup-choices.json"): print("No python-setup-choices.json to make choices. Please make that file."); exit(-1)
print("\033c", end="")

while True:
    try:
        ops = json.load(open(os.path.join(current_dir, "python-setup-choices.json"), "r"))["choices"]
        opstr = "\n"
        counter = 1
        for option in ops:
            opstr += f"{counter}: {option[1]}\n"
            counter += 1

        try:option = int(input(f"Enter option: {colorama.Fore.LIGHTBLUE_EX}{opstr}{colorama.Fore.RESET}->"))
        except ValueError: print("\033c", end="");print("Invalid")
        else:
            print("\033c", end="")
            if option > len(ops) or option < 1:
                print("\033c", end="");print("Please enter the right number of your choice")
            else:
                if ops[option-1][2] == "dir":
                    if os.path.exists(os.path.join(current_dir, ops[option-1][0], "python-setup-file.bat")): subprocess.run(os.path.join(current_dir, ops[option-1][0], "python-setup-file.bat"), shell=True)
                    elif os.path.exists(os.path.join(current_dir, ops[option-1][0], "python-setup-choices.json")):current_dir = os.path.join(current_dir, ops[option-1][0])
                    else: print("\033c", end="");print("The directory you chose does not have a python-setup-file.bat or python-setup-choices.json")
                elif ops[option-1][2] == "file":
                    subprocess.run(os.path.join(current_dir, ops[option-1][0]), shell=True)
    except KeyboardInterrupt:
        exit(0)