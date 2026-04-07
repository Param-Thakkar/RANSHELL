import configparser
import os
import concurrent.futures


def write_directory_paths_to_file(directory, output_file, max_workers=None):
    with open(output_file, 'w') as file:
        file.write(directory + '\n')  
        for root, dirs, _ in os.walk(directory):
            print('working')
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                file.write(dir_path + '\n')



config = configparser.ConfigParser()
config.read('config.ini')

directory_path = config['Settings']['directory_path']
accessible_paths_output_txt_file = 'accessible_paths.txt'
max_workers_value = int(config['Settings']['cores_selected'])

write_directory_paths_to_file(directory_path, accessible_paths_output_txt_file, max_workers=max_workers_value)
