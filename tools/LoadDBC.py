import cantools

from can.message import Message
db = cantools.db.load_file('/home/aaron/workspace/CAN_dev/toyota_camry_hybrid_2018_pt_generated.dbc')
print(db)

msg = db.get_message_by_name('EPS_STATUS')
print(msg)
