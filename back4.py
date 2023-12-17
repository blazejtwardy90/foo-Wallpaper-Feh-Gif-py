#!/usr/bin/python3

import subprocess
import hashlib
import os
import sys
from time import sleep

class Command():
    FEHCOMMAND = ['feh','--bg-fill', '--no-fehbg']
    XWALLPAPERCOMMAND=['xwallpaper','--zoom']
    XLOADIMAGE=['xloadimage', '-onroot', '-fullscreen']
    UBUNTUXFCCOMMAND = ['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitor0/workspace0/last-image', '-s']

FREMESPERSECOND = 30

def createHash(file_path: str):
    file_path = file_path.encode(encoding="utf-8")
    hash_path = hashlib.md5(file_path).hexdigest()
    return hash_path

def createHashDir(dir_to_created):
    dir_created = False
    try:
        os.makedirs(dir_to_created, exist_ok=False)
        dir_created = True
    except FileExistsError:
        dir_created = False
    
    return dir_created

def main(arg1, arg2):
    speed = str(arg1).lower()
    file_path = str(arg2)
    used_program = Command.FEHCOMMAND
    
    created_hash = createHash(file_path)
    create_dir = 'tmp/' + created_hash
    new_dir_created = createHashDir(create_dir)
    
    if new_dir_created == True:
        subprocess.run(['convert', '-coalesce', file_path, f'{create_dir}/{created_hash}.png'])
    
    only_files = next(os.walk(create_dir))[2]
    amount_of_frames = len(only_files)
    if speed == 'auto' or speed == None:
        speed = amount_of_frames/FREMESPERSECOND * 1/FREMESPERSECOND
    else:
        speed = float(speed)
    
    try:
        while True:
            for index in range(amount_of_frames):
                full_command = used_program + [f'{create_dir}/{created_hash}-{index}.png']
                subprocess.run(full_command)
                sleep(speed) 
    except KeyboardInterrupt:
        print("Bye...")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
