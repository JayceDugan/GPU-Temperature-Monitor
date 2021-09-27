#!/usr/bin/env python3

import time
import sys
import schedule
from gpu import check_temperature
from process import check_is_running

def initialise_scheduler():
    schedule.every(30).seconds.do(check_temperature)

    while True:
        schedule.run_pending()
        time.sleep(1)

def init():
    if check_is_running('app_nhm.exe') and check_is_running('OpenHardwareMonitor.exe'):
        print('Nicehash miner and open hardware monitor found, initialising GPU monitor.')
        check_temperature()
        initialise_scheduler()
    else:
        print('Nicehash (app_nhm.exe) or Open Hardware Monitor (OpenHardwareMonitor.exe) not found in running processes, exiting.')
        sys.exit()


# Miner go brr
init()