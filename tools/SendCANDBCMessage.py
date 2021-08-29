import cantools
import can

from can.message import Message
from cantools.database.can import attribute
db = cantools.db.load_file('/home/aaron/workspace/CAN_dev/toyota_camry_hybrid_2018_pt_generated.dbc')

msg = db.get_message_by_name('BRAKE_MODULE')
msg_data = msg.encode({'BRAKE_PRESSURE':1,'BRAKE_POSITION':1,'BRAKE_PRESSED':1})

canbus = can.interface.Bus(bustype='socketcan',channel='vcan0',bitrate=250000)
msg = can.Message(arbitration_id=msg.frame_id, data=msg_data,is_extended_id=False)

try:
    canbus.send(msg)
    print('Message sendt on {}'.format(canbus.channel_info))

except can.CanError:
    print('Message NOT sent.')