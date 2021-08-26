import can

canbus = can.interface.Bus(bustype='socketcan', 
                           channel='vcan0', 
                           bitrate=500000)
sendMessage = can.Message(arbitration_id=0x01,
                      data=[0,25,0,1,3,1,4,1],
                      is_extended_id=False)

try:
    canbus.send_periodic(sendMessage,1)
    print('Message sent on {}'.format(canbus.channel_info))

    while True:
        receivedMessage = canbus.recv()
        print(receivedMessage)

        if receivedMessage.arbitration_id == 0x0001:
            replyMessage = can.Message(arbitration_id=0x02,
                                       data=[190,239,222,173],
                                       is_extended_id=False)
            canbus.send(replyMessage)


except can.CanError:
    print('Message NOT sent!')