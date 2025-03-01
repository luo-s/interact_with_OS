#!/usr/bin/env python3
import sys
import subprocess

# change 'jane' to 'jdoe' 

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
        old_value = line.strip()
        new_value = old_value.replace('jane', 'jdoe')
        subprocess.run(['mv', old_value, new_value])

# to execute:
# ./changeJane.py oldFiles.txt