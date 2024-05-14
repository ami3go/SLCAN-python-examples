import time
import can
import cantools

db = cantools.database.load_file('DBC_Example.dbc')
# print(db.messages)
global can_bus

def can_init():
    global can_bus
    print("Attaching vector box CH1 to application."
          "Please make sure that in Vector Hardware configuration correct channel attached to 'python-can' application")
    can_bus = can.interface.Bus(bustype="vector",
                            channel=[0],
                            bitrate=500000,
                            app_name="python-can")
def can_get_msg():
    global can_bus
    message = can_bus.recv()
    can_decode = db.decode_message(message.arbitration_id, message.data)
    return can_decode

def get_freq_and_level():
    global can_bus
    val = {
        "EMV_Pegel": 0,
        "EMV_Frequenz": 0,
    }
    for i in range(10):
        var = can_get_msg()
        if 'EMV_Pegel' in var.keys():
            val["EMV_Pegel"] = var["EMV_Pegel"]
        if 'EMV_Frequenz' in var.keys():
            val['EMV_Frequenz'] = var['EMV_Frequenz']
        if val['EMV_Frequenz'] != 0 and val["EMV_Pegel"] != 0:
            return val
        time.sleep(0.05)


if __name__ == "__main__":
    can_init()
    print("init done")

    for i in range(100):
        print(get_freq_and_level())

