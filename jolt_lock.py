import json
import os
import subprocess
import time

# Threshold for detecting a jolt (adjustable)
JOLT_THRESHOLD = 15.0  # Change based on sensitivity

def get_accelerometer_data():
    """Fetch accelerometer data using Termux API."""
    try:
        # Use termux-sensor to get accelerometer data
        result = subprocess.check_output(['termux-sensor', '-s', 'Accelerometer', '-n', '1'], text=True)
        data = json.loads(result)
        return data['Accelerometer']
    except Exception as e:
        print(f"Error fetching accelerometer data: {e}")
        return None

def lock_phone():
    """Lock the phone by simulating a lock action."""
    os.system("termux-tts-speak 'Locking phone due to sudden jolt.'")
    os.system("input keyevent 26")  # This simulates pressing the power button to lock the phone

def monitor_jolts():
    """Continuously monitor accelerometer data and lock phone on jolt."""
    print("Monitoring for jolts...")
    while True:
        sensor_data = get_accelerometer_data()
        if sensor_data:
            x = sensor_data['values'][0]
            y = sensor_data['values'][1]
            z = sensor_data['values'][2]
            
            # Calculate the magnitude of the acceleration vector
            magnitude = (x**2 + y**2 + z**2) ** 0.5
            print(f"Acceleration magnitude: {magnitude}")
            
            if magnitude > JOLT_THRESHOLD:
                print("Jolt detected! Locking phone...")
                lock_phone()
                time.sleep(5)  # Add a delay to prevent multiple locks in quick succession
        time.sleep(0.1)  # Adjust polling frequency as needed

if __name__ == "__main__":
    monitor_jolts()
