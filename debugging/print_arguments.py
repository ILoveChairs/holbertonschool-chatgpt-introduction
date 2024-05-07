#!/usr/bin/python3
import sys
import os

filename = os.path.splitext(sys.argv[0])[0]
print(filename)

for i in range(1, len(sys.argv)):
    print(sys.argv[i])

