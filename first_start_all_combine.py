import os
import configparser
import subprocess
import time
import tkinter as tk
from tkinter import ttk, filedialog

def check_first_run():
    config_file = 'config.ini'

    config = configparser.ConfigParser()

    if not os.path.exists(config_file):
        config['DEFAULT'] = {'first_run': 'False'}
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        return True
    else:
        config.read(config_file)
        first_run = config['DEFAULT'].getboolean('first_run', fallback=False)

        if first_run:
            config['DEFAULT']['first_run'] = 'False'
            with open(config_file, 'w') as configfile:
                config.write(configfile)
        
        return first_run


if check_first_run():
    print("First run!")
     
    class App(tk.Tk):
        def __init__(self):
            super().__init__()

            self.title("Combined Functionality")
            self.geometry("400x250")

            self.max_value = os.cpu_count()
            self.create_cores_selector()
            self.create_directory_selector()
            self.create_continue_button()

        def create_cores_selector(self):
            cores_frame = ttk.Frame(self)
            cores_frame.pack(padx=10, pady=10)

            slider_label = ttk.Label(cores_frame, text="Select the No. of cores to be used:")
            slider_label.pack()

            self.selected_value_label = ttk.Label(cores_frame, text=f"No. of cores to be used: 1")
            self.selected_value_label.pack()

            self.slider = ttk.Scale(cores_frame, from_=1, to=self.max_value, orient="horizontal", length=300, command=self.on_slider_update)
            self.slider.pack()

            self.value_entry = ttk.Entry(cores_frame)
            self.value_entry.pack()

            self.value_entry.bind("<Return>", self.update_from_textbox)
            self.value_entry.bind("<KeyRelease>", self.update_from_textbox)

        def on_slider_update(self, value):
            rounded_value = round(float(value))
            self.selected_value_label.config(text=f"No. of cores to be used: {rounded_value}")
            self.value_entry.delete(0, tk.END)
            self.value_entry.insert(0, str(rounded_value))

        def create_directory_selector(self):
            def update_config_ini(directory_path):
                config_file = 'config.ini'
                config = configparser.ConfigParser()
                config.read(config_file)
                
                if 'Settings' not in config:
                    config['Settings'] = {}
                config['Settings']['directory_path'] = directory_path
                
                with open(config_file, 'w') as configfile:
                    config.write(configfile)

            def select_directory():
                selected_directory = filedialog.askdirectory()
                if selected_directory:
                    update_config_ini(selected_directory)

            directory_frame = ttk.Frame(self)
            directory_frame.pack(padx=10, pady=10)

            select_button = ttk.Button(directory_frame, text="Select Directory", command=select_directory)
            select_button.pack()

        def create_continue_button(self):
            def continue_action():
                selected_cores = int(self.slider.get())
                config_file = 'config.ini'
                config = configparser.ConfigParser()
                config.read(config_file)
                if 'Settings' not in config:
                    config['Settings'] = {}
                config['Settings']['cores_selected'] = str(selected_cores)
                
                with open(config_file, 'w') as configfile:
                    config.write(configfile)
                
                config.read(config_file)
                selected_directory = config.get('Settings', 'directory_path', fallback='Not selected')
                print(f"Selected cores: {selected_cores}")
                print(f"Selected directory: {selected_directory}")
                time.sleep(2)
                subprocess.run(['python', 'all_moveing_parts.py'])
                self.destroy()
                
            continue_frame = ttk.Frame(self)
            continue_frame.pack(padx=10, pady=10)

            continue_button = ttk.Button(continue_frame, text="Continue", command=continue_action)
            continue_button.pack()

        def update_from_textbox(self, event=None):
            try:
                value = int(self.value_entry.get())
                if 1 <= value <= self.max_value:
                    self.slider.set(value)
                    self.selected_value_label.config(text=f"No. of cores to be used: {value}")
                else:
                    self.selected_value_label.config(text="You don't have that many cores!")
            except ValueError:
                self.selected_value_label.config(text="Invalid value!")
        

    app = App()
    app.mainloop()

else:
 print("Not the first run!")
    
