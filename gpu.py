import wmi
import sys
from datetime import datetime

from twilio_api import send_message
from process import kill_process

gpu_highest_temperature = 0

def kill_nicehash_miner():
    kill_process('app_nhm.exe')

def load_gpu_temp():
    gpu_temp = 0
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
    sensors = w.Sensor()

    for sensor in sensors:
        if sensor.SensorType == u'Temperature' and 'GPU Hot Spot' in sensor.Name:
            gpu_temp = sensor.Value

    return gpu_temp

def check_temperature():
    global gpu_highest_temperature
    gpu_safe_temperature = 65
    gpu_current_temperature = load_gpu_temp()
    gpu_is_fiery_boi = gpu_current_temperature >= gpu_safe_temperature

    if gpu_current_temperature > gpu_highest_temperature:
      gpu_highest_temperature = gpu_current_temperature

    print('-------')
    print('Gpu checked: (' + datetime.now().strftime("%H:%M:%S") + '): current temp: ' + str(gpu_current_temperature) + "\u00b0" + ', highest temp: ' + str(gpu_highest_temperature) + "\u00b0")

    if gpu_is_fiery_boi:
        kill_nicehash_miner()
        send_message("Nicehash miner killed: current GPU Temp: {}\u00b0".format(gpu_current_temperature))
        sys.exit()
