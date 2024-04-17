#!/usr/bin/python3
import sys

current_key = None
current_count = 0
key = None


for line in sys.stdin:
    line = line.strip()
    key, count = line.split(',')

    try:
        count = int(count)
    except ValueError:
        continue

    if current_key == key:
        current_count += count
    else:
        if current_key:
            split_key = current_key.split("_")
            product = split_key[0]
            location = split_key[1]
            print(f'{product},{location},{current_count}')
        
        current_count = count
        current_key = key

if current_key == key:
    split_key = current_key.split("_")
    product = split_key[0]
    location = split_key[1]
    print(f'{product},{location},{current_count}')