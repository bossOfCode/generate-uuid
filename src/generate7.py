import os
import sys
import time
import secrets as hex

def insert(str1, str2, index):
  orginal = str1
  new = str2
  pos = index

  global output
  output = original[:pos] + new + original[pos:]

uuid = ''
next = ''

epoch = format(time.time() * 1000, 'x')

uuid = '0' + epoch + '-'

insert(uuid, '-', 7)
uuid = output + '7'

next = hex.token_hex(1.5)
uuid = uuid + next + '-b'

next = hex.token_hex(1.5)
uuid = uuid + next + '-'

next = hex.token_hex(6)
uuid = uuid + next
