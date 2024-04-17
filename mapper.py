#!/usr/bin/python3
import sys

for line in sys.stdin:
    
    line = line.strip() # Hilangkan whitespace
    data = line.split(",")
    product = data[2]
    location = data[1]

    print(f"{product}_{location},{1}")