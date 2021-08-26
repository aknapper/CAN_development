import can
from can import bus

canbus = can.interface.Bus(bustype='socketcan', 
                           channel='vcan0', 
                           bitrate=500000)
message = can.Message(arbitration_id=0xc0ffee,
                      data=[0,25,0,1,3,1,4,1],
                      is_extended_id=False)

try:
    canbus.send_periodic(message,1)
    print('Message sent on {}'.format(canbus.channel_info))

    while True:
        message = canbus.recv()
        print(message)
except can.CanError:
    print('Message NOT sent!')