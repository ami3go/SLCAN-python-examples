import time
import can

bus = can.interface.Bus(bustype='slcan',
                        channel='/dev/ttyACM1',
                        bitrate=500000,
                        ttyBaudrate=115200,
                        timeout=2,
                        )
z =0
while True:
    msg = bus.recv(1)
    if msg != None:
        z = z +1
        print(z,msg)

bus.shutdown()