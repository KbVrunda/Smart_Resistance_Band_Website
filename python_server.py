import asyncio
import websockets
import serial

# terminal line to find port
# for Mac: 
# ls /dev/tty.usb*

# For windows: 
# Get-WmiObject Win32_SerialPort

# run server. Edit with your own path 
# python '/Users/vrundapatel/Desktop/BME 261L/python_server.py'

# ----- SETUP -----
SERIAL_PORT = '//dev/tty.usbmodem11301' # Adjust to match your system
BAUD_RATE = 9600
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Only takes 1 argument now (no path!)
async def send_serial_force_data(websocket):
    print("Client connected")
    try:
        while True:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                print("Sending:", line)
                await websocket.send(line)
            await asyncio.sleep(0.1)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    server = await websockets.serve(send_serial_force_data, "localhost", 8765)  # No lambda, no path
    print("WebSocket server running on ws://localhost:8765")
    await server.wait_closed()

asyncio.get_event_loop().run_until_complete(main())
