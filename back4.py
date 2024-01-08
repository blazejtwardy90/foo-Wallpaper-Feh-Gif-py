#!/usr/bin/env python3

import subprocess
from hashlib import md5
import os
import sys
from time import sleep
import threading
import dbus

class Command():
    FEHCOMMAND = ['feh','--bg-fill', '--no-fehbg']
    XWALLPAPERCOMMAND=['xwallpaper','--zoom']
    XLOADIMAGE=['xloadimage', '-onroot', '-fullscreen']
    UBUNTUXFCCOMMAND = ['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitor0/workspace0/last-image', '-s']

FREMESPERSECOND = 30

screen_lock_event = threading.Event()

def isScreenLocked():
    bus = dbus.SessionBus()
    desktop_environment = os.environ.get('DESKTOP_SESSION')
    
    match desktop_environment:
        case 'cinnamon':
            screensaver_proxy = bus.get_object('org.cinnamon.ScreenSaver', '/org/cinnamon/ScreenSaver')
            screensaver_interface = dbus.Interface(screensaver_proxy, 'org.cinnamon.ScreenSaver')
        case _:
            screensaver_proxy = bus.get_object('org.freedesktop.ScreenSaver', '/org/freedesktop/ScreenSaver')
            screensaver_interface = dbus.Interface(screensaver_proxy, 'org.freedesktop.ScreenSaver')
    
    return bool(screensaver_interface.GetActive())

def screenCheck(shared_variable):
    while shared_variable['stop'] == False:
        if isScreenLocked():
            #Screen is locked. Setting event to pause animation
            screen_lock_event.clear()
        else:
            #Screen is unlocked. Setting event to resume animation
            screen_lock_event.set()
        sleep(3) 
    print("Screen Check Stopped")

def createHash(file_path: str):
    file_path = file_path.encode(encoding="utf-8")
    hash_path = md5(file_path).hexdigest()
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
    shared_variable = {'stop': False}
    screen_check_thread = threading.Thread(target=screenCheck, args=(shared_variable,))
    screen_check_thread.start()

    used_program = Command.FEHCOMMAND
    
    created_hash = createHash(file_path)
    create_dir = 'tmp/' + created_hash
    new_dir_created = createHashDir(create_dir)
    
    if new_dir_created == True:
        print("Creating frames")
        subprocess.run(['convert', '-coalesce', file_path, f'{create_dir}/{created_hash}.png'])
    else:
        print("Dir already created")
    
    only_files = next(os.walk(create_dir))[2]
    amount_of_frames = len(only_files)
    if speed == 'auto' or speed == None:
        speed = amount_of_frames/FREMESPERSECOND * 1/FREMESPERSECOND
    else:
        speed = float(speed)
    
    try:
        while True:
            screen_lock_event.wait()
            for index in range(amount_of_frames):
                full_command = used_program + [f'{create_dir}/{created_hash}-{index}.png']
                subprocess.run(full_command)
                sleep(speed) 
    except KeyboardInterrupt:
        print("Bye...")
    finally:
        shared_variable['stop'] = True
        screen_check_thread.join()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("No arguments foun ending program")
    else:
        main(sys.argv[1], sys.argv[2])
