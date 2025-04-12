import time  # Importing time module for working with time-related functions
import random  # Importing random module to generate random numbers
import json  # Importing json module to handle JSON data
from azure.iot.device import IoTHubDeviceClient, Message  # Importing necessary Azure IoT libraries

# Connection string for the IoT device
CONNECTION_STRING = "HostName=romeoIOT.azure-devices.net;DeviceId=sensor2;SharedAccessKey=galAxhlJv5vJoopMnUvPnIhC6vHaLBNtQd9eXjcVDSw="

# Function to simulate getting sensor data
def get_sensor_data():
    """
    Generates random sensor data including ice thickness, air temperature, and wind speed.
    Returns a dictionary with this data.
    """
    return {
        "deviceId": "sensor-rideau-002",  # Device ID
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),  # Timestamp in UTC format
        "iceThicknessCm": round(random.uniform(10.0, 35.0), 1),  # Random ice thickness between 10 and 35 cm
        "airTemperatureC": round(random.uniform(-25.0, 5.0), 1),  # Random air temperature between -25 and 5°C
        "windSpeedKmh": round(random.uniform(0.0, 30.0), 1)  # Random wind speed between 0 and 30 km/h
    }

def main():
    """
    Main function that connects to the Azure IoT Hub, sends the sensor data repeatedly,
    and handles disconnection upon termination.
    """
    # Create a client to connect to the IoT Hub using the device's connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending sensor data to IoT Hub...")
    
    try:
        while True:
            # Get new sensor data
            data = get_sensor_data()
            # Convert the sensor data to a JSON string
            message = Message(json.dumps(data))
            # Send the message to the IoT Hub
            client.send_message(message)
            # Print the sent message for confirmation
            print(f"Sent message: {data}")
            # Wait for 5 seconds before sending the next message
            time.sleep(5)
    except KeyboardInterrupt:
        # If the program is interrupted (Ctrl + C), stop sending messages
        print("Stopped sending messages.")
    finally:
        # Ensure the client is properly disconnected after the program finishes
        client.disconnect()

# Entry point of the program. It will run the main function when the script is executed.
if __name__ == "__main__":
    main()
