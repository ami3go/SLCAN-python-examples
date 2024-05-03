import time
from can import Message
msg = Message(arbitration_id=0x00,
                  data=[0, 25, 0, 1, 3, 1, 4, 1],
                  is_extended_id=True)
print(msg)