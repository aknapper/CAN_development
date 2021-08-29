import cantools

from can.message import Message
import can

db = cantools.db.load_file('/home/aaron/workspace/CAN_development/toyota_camry_hybrid_2018_pt_generated.dbc')

canbus = can.interface.Bus(bustype="socketcan", channel='vcan0', bitrate=250000)

while True:
    message = canbus.recv()
    decodedmsg = db.decode_message(message.arbitration_id, message.data)
    print(decodedmsg)