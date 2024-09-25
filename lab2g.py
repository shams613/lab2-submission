#!/usr/bin/env python3
# Author: Shams Bin Harun
# Author ID: sbharun
# Date Created: 2024/09/25

import sys

# Default value for timer
timer = 3

# Check if an argument is provided
if len(sys.argv) == 2:
    try:
        timer = int(sys.argv[1])
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)

# Loop until timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

