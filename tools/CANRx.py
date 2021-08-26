import can

canbus = can.interface.Bus(bustype='socketcan', 
                           channel='vcan0', 
                           bitrate=500000)

while True:
    message = canbus.recv()
    print(message)