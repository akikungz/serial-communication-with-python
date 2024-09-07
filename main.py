from serial import Serial

serial = Serial('/dev/ttyUSB0', 9600)

while True:
    data = serial.readline()
    print(data)
    
    if data == b'exit\n':
        break

serial.close()