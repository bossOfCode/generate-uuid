"""import"""
import os
import time

OUTPUT = ''

def insert(str1, str2, index):
    "insert text at index"
    original = str1
    new = str2
    pos = index

    global OUTPUT
    OUTPUT = original[:pos] + new + original[pos:]

def print_in_os(argument):
    "print in both terminal and action logs"
    print(argument)
    os.system(argument)


print_in_os("echo Version 7")

UUID = ''
ADD = ''

EPOCH = round(time.time() * 1000)
EPOCHMILLI = format(EPOCH, 'x')

UUID = '0' + EPOCHMILLI + '-'

insert(UUID, '-', 8)
UUID = OUTPUT + '7'

ADD = os.urandom(2).hex()[:-1]
UUID = UUID + ADD + '-'

ADD = os.urandom(2).hex()
UUID = UUID + ADD + '-'

ADD = os.urandom(6).hex()
UUID = UUID + ADD

print_in_os(f"echo 'uuid={UUID}' >> $GITHUB_OUTPUT")
print_in_os("echo 'safe=safe' >> $GITHUB_OUTPUT")
