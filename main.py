from serial import Serial
from threading import Thread

port = input("Enter the port (Example: COM3, /dev/ttyUSB0): ")
bund = input("Enter the baudrate (Example: 9600, 115200): ")

if (port == "" or bund == ""):
    print("You must enter a port and a baudrate.")
    exit()

if (not bund.isdigit()):
    print("The baudrate must be a number.")
    exit()

# Serial input thread
def serial_input():
    while True:
        ser.write(input().encode("utf-8") + b"\n")

with Serial(port, int(bund)) as ser:
    # Start the serial input thread
    input_thread = Thread(target=serial_input)
    
    while True:
        input_thread.start()
        if ser.in_waiting > 0:
            print(ser.readline().decode("utf-8").strip())
            # Destroy the serial input thread
            input_thread.join()