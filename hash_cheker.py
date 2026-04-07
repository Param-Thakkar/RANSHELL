import os
import hashlib
import time
import tkinter as tk
from tkinter import messagebox

st = time.process_time()

def calculate_file_sha256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()

def verify_hashes(hash_file):
    root = tk.Tk()  
    root.withdraw()  

    for line in open(hash_file, 'r'):
        file_path, stored_hash = line.strip().split(': ')
        if not os.path.exists(file_path):
            print(f"File {file_path} not found.")
            continue

        calculated_hash = calculate_file_sha256(file_path)
        if calculated_hash == stored_hash:
            print(f"{file_path}: Hash matches!")
        else:
            print(f"{file_path}: Hash doesn't match!"+calculated_hash)
            messagebox.showerror("Hash Mismatch", f"Hash doesn't match for '{file_path}' '{calculated_hash}' ")
            print(f"{file_path}: Hash doesn't match!"+calculated_hash)
clear = lambda: os.system('cls')

hello=2
while hello == 2:
    verify_hashes('D:\PARAM CODE\RANSHELL\Ranshell python intigreate\hash.ranshell')
    time.sleep(0.25)
    et = time.process_time()
    res = et - st
    print('CPU Execution time:', res, 'seconds')

    