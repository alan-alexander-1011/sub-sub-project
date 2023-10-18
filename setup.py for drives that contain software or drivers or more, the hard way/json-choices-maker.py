'''
if you want to make the json file from typing just use this template:
{
    "choices": [
        ["The directory/file name with extension", "The name you want to show", "the type of that: 'dir' or 'file'"],
        ...
    ]
}
'''
import json
import os

curr_file_path = os.path.dirname(os.path.abspath(__file__))

opt = input("Enter the directory you want to make the json file, just the name\n(at the directory of the file that you are running), current directory, type '.' .\n ->")
if os.path.exists(os.path.join(curr_file_path, opt)):
    path_chosen = os.path.join(curr_file_path, opt)
    if os.path.exists(path_chosen):
        pass
    else: exit(-1)
    dir_chosen = os.listdir(path_chosen)
    temp_json_str = ""
    for directory in dir_chosen:
        if os.path.isfile(os.path.join(path_chosen, directory)):
            temp_json_str += f'["{directory}","{os.path.splitext(directory)[0]}","file"],'
        elif os.path.isdir(os.path.join(path_chosen, directory)):
            temp_json_str += f'["{directory}","{directory.capitalize()}","dir"],'
        else:pass
    json_str = rf"{{'choices': [{temp_json_str.rstrip(',')}]}}"
    print(json_str)
    json_str = json.loads(json_str.replace("'", "\""))
    with open(os.path.join(path_chosen, "python-setup-choices.json"), "w+", encoding="utf-8") as f:
        json.dump(json_str, f, indent=4)

print("Success. If you want to change more, go into that directory and change your settings.")

