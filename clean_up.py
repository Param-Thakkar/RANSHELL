import os

file_paths_file = "files.ranshell"  
hash_file = "hash.ranshell"  
dir_file = "dir.ranshell"
config_ini = ""

if os.path.exists(file_paths_file):
    with open(file_paths_file, 'r') as file:
        
        for line in file:
            file_path = line.strip()  
            
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            else:
                print(f"The file '{file_path}' does not exist.")

    
    os.remove(file_paths_file)
    print(f"File '{file_paths_file}' has been deleted.")
else:
    print(f"The file '{file_paths_file}' does not exist.")


if os.path.exists(hash_file):
    os.remove(hash_file)
    print(f"File '{hash_file}' has been deleted.")
else:
    print(f"The file '{hash_file}' does not exist.")

if os.path.exists(dir_file):
    os.remove(dir_file)
    print(f"File '{dir_file}' has been deleted.")
else:
    print(f"The file '{dir_file}' does not exist.")

if os.path.exists(dir_file):
    os.remove(dir_file)
    print(f"File '{dir_file}' has been deleted.")
else:
    print(f"The file '{dir_file}' does not exist.")

import configparser

def create_initial_config():
    config = configparser.ConfigParser()

    config['DEFAULT'] = {'first_run': 'True'}
    config['Settings'] = {'cores_selected': '',
                          'directory_path': ''}
    config['Install'] = {'install_type': 'normal'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

create_initial_config()