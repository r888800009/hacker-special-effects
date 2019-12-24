#!/usr/bin/env python
import sys
import time
import random


stdin_str = str(sys.stdin.read())

out_buffer = ''
out_size = random.randint(3, 20)

for i in stdin_str:
    out_buffer += i
    out_size -= 1
    if out_size == 0:
        print(out_buffer, end='',flush=True)
        time.sleep(0.005)
        out_size = random.randint(1, 30)
        out_buffer = ''

print(out_buffer, end='',flush=True)
