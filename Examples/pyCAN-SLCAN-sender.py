import time
import can
import random

bus = can.interface.Bus(bustype='slcan',
                        channel='/dev/ttyACM0',
                        bitrate=500000,
                        ttyBaudrate=115200,
                        timeout=2,
                        )

for z in range(10000):
    a = random.randint(0,254)
    msg = can.Message(arbitration_id=0x11,
                  data=[a, 25, 0, 1, 3, 1, 4, a],
                  is_extended_id=False
                      )

    bus.send(msg, 1)
    print(z, msg)
    time.sleep(1)
bus.shutdown()