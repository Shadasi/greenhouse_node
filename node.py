import time
import smbus2
import os

import requests
import json

from dotenv import load_dotenv, find_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv(find_dotenv())

API_URL = os.environ.get("API_URL")
SENSOR_NAME = os.environ.get("SENSOR_NAME")
POLL_INTERVAL = os.environment.get("POLL_INTERVAL")


headers = {
    'Content-Type': 'application/json'
}

address = 0x38

i2cbus = smbus2.SMBus(1)
time.sleep(0.5)

def PostTemp(temp):
    response = requests.request("POST", API_URL + 'temp', headers=headers, data=json.dumps({"temp": temp, "sensorName": SENSOR_NAME, "timestamp": int(time.time())}))
    print(response)

def PostHumidity(humidity):
    response = requests.request("POST", API_URL + 'humidity', headers=headers, data=json.dumps({"humidity": humidity, "sensorName": SENSOR_NAME, "timestamp": int(time.time())}))
    print(response)

def readTempAndHumididty():
    # credit: https://raspberrypi.stackexchange.com/a/133487
    data = i2cbus.read_i2c_block_data(address,0x71,1)
    if(data[0] | 0x08) == 0:
        print('Initialization Error')

    i2cbus.write_i2c_block_data(address,0xac,[0x33,0x00])
    time.sleep(0.1)

    data = i2cbus.read_i2c_block_data(address,0x71,7)

    Traw = ((data[3] & 0xf) << 16 ) + (data[4] << 8) + data[5]
    temperature = 200*float(Traw)/2**20 - 50
    fahrenheit = ((temperature * (9/5)) + 32)

    Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
    humidity = 100*float(Hraw)/2**20
    print("%.1f" % fahrenheit)
    print(humidity)

    PostTemp(fahrenheit)
    time.sleep(0.5)
    PostHumidity(humidity)

def __main__():
    while True:
        readTempAndHumididty()
        time.sleep(POLL_INTERVAL)

__main__()


