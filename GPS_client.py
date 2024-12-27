import subprocess
import json
import requests
import time

# Configuration
REMOTE_SERVER_URL = "https://your-remote-server.com/endpoint"  # Replace with your server's URL
TRACKING_INTERVAL = 10  # Interval in seconds to send GPS data

def get_gps_location():
    """Fetch GPS location using Termux API."""
    try:
        # Execute Termux command to get location
        result = subprocess.check_output(['termux-location'], text=True)
        location_data = json.loads(result)

        # Extract relevant GPS data
        latitude = location_data["latitude"]
        longitude = location_data["longitude"]
        accuracy = location_data["accuracy"]

        return {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": accuracy,
            "timestamp": location_data["time"]
        }
    except Exception as e:
        print(f"Error fetching GPS data: {e}")
        return None

def send_data_to_server(data):
    """Send GPS data to the remote server."""
    try:
        response = requests.post(REMOTE_SERVER_URL, json=data)
        if response.status_code == 200:
            print(f"Data sent successfully: {data}")
        else:
            print(f"Failed to send data. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

def main():
    """Main function to continuously track and send GPS data."""
    print("Starting GPS tracking...")
    while True:
        gps_data = get_gps_location()
        if gps_data:
            print(f"GPS Data: {gps_data}")
            send_data_to_server(gps_data)
        else:
            print("Unable to fetch GPS data.")
        
        time.sleep(TRACKING_INTERVAL)

if __name__ == "__main__":
    main()
