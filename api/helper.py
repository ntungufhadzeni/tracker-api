from datetime import datetime

import requests
from environs import Env

env = Env()
env.read_env()

BASE_URL = env.str("TRACKER_URL")
USERNAME = env.str("TRACKER_USERNAME")
PASSWORD = env.str("TRACKER_PASSWORD")


def rename_vehicle(vehicle_id):
    vehicle_id = int(vehicle_id)
    if vehicle_id < 10:
        return '00' + str(vehicle_id)
    elif vehicle_id >= 10:
        return '0' + str(vehicle_id)


def get_vehicle_position(vehicle_id: str):
    vehicles = {
        "007": 9,
        "015": 10,
        "014": 12,
        "012": 13,
        "013": 14,
        "005": 15,
        "018": 16,
        "008": 17,
        "003": 18,
        "016": 19,
        "004": 20,
        "011": 22,
        "001": 23,
        "002": 24,
        "020": 26,
        "010": 27,
        "009": 28,
        "017": 29,
        "021": 30,
        "006": 36,
        "019": 41,
    }
    device_id = vehicles[vehicle_id]
    today = datetime.now().date().strftime('%Y-%m-%dT%H:%M:%SZ')
    params = {'deviceId': device_id, 'from': today}
    res = requests.get(f'{BASE_URL}/positions', params=params, auth=(USERNAME, PASSWORD))
    devices = res.json()
    return devices[0]["latitude"], devices[0]["longitude"]
