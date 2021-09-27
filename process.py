import os
import psutil

def check_is_running(process_name):
    for proc in psutil.process_iter():
        try:
            # Check if the process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProces):
            pass

    return False

def kill_process(process_name):
    os.system("taskkill /f /t /im {}".format(process_name))

