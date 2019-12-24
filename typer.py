#!/usr/bin/env python
import sys
import time
import random


stdin_str = str(sys.stdin.read())

out_buffer = ''
min_size, max_size = 3, 20
out_size = random.randint(min_size, max_size)

for i in stdin_str:
    out_buffer += i
    out_size -= 1
    if out_size == 0:
        print(out_buffer, end='',flush=True)
        time.sleep(0.005)
        out_size = random.randint(min_size, max_size)
        out_buffer = ''

print(out_buffer, end='',flush=True)
