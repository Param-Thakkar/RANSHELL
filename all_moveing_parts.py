import configparser
import os
import concurrent.futures
import random
import string
import subprocess
import time
import hashlib

Rand_file_extensions = ['.xlsx', '.docx', '.pptx', '.jpeg', '.png', '.jpeg', '.gif', '.dwg']
generated_files = []  
config = configparser.ConfigParser()
config.read('config.ini')
directory_path = config['Settings']['directory_path']
accessible_paths_output_txt_file = 'dir.ranshell'
file_paths_file = 'files.ranshell'
max_workers_value = int(config['Settings']['cores_selected'])
if max_workers_value <= 0:
    max_workers_value = 1

def write_directory_paths_to_file(directory, output_file, max_workers=None):
    with open(output_file, 'w') as file:
        file.write(directory + '\n')  
        for root, dirs, _ in os.walk(directory):
            print('working')
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                file.write(dir_path + '\n')
def create_random_text_file(directory):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=128))
    file_extension = random.choice(Rand_file_extensions)
    rand_file_name = ''.join(random.choices(string.ascii_letters, k=3)) + file_extension  
    file_name = 'DO_NOT_DELET ' + rand_file_name
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(random_string)
    generated_files.append(file_path)  

def process_directories_file(file_path, max_workers=None):
    with open(file_path, 'r') as file:
        directories = file.readlines()
        directories = [directory.strip() for directory in directories]

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            for directory in directories:
                executor.submit(create_random_text_file, directory)

    
    with open('files.ranshell', 'w') as rand_files:
        for file_path in generated_files:
            rand_files.write(file_path + '\n')
def calculate_file_sha256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return file_path, hasher.hexdigest()

def process_files_for_hashes(file_paths_file, max_workers=None):
    with open(file_paths_file, 'r') as file:
        file_paths = file.readlines()
        file_paths = [path.strip() for path in file_paths]

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            hash_results = {executor.submit(calculate_file_sha256, file_path): file_path for file_path in file_paths}

            with open('hash.ranshell', 'w') as hash_file:
                for future in concurrent.futures.as_completed(hash_results):
                    file_path = hash_results[future]
                    try:
                        file_path, hash_value = future.result()
                        print(f"File: {file_path}, Hash: {hash_value}") 
                        hash_file.write(f"{file_path}: {hash_value}\n")
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")

write_directory_paths_to_file(directory_path, accessible_paths_output_txt_file, max_workers=max_workers_value)
time.sleep(3)
directories_file = 'dir.ranshell'
process_directories_file(directories_file, max_workers=max_workers_value)
time.sleep(3)
process_files_for_hashes(file_paths_file, max_workers=max_workers_value)
time.sleep(10)
exit()
#subprocess.run(['python', 'hash_cheker.py'])