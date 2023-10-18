#!/usr/bin/python3

import random

# Generate random 4 digit binary
bin_num = ''
for i in range(4):
    bin_num += str(random.randint(0, 1))

# Convert binary to decimal
deci_num = 0
for i in range(len(bin_num)):
    deci_num += int(bin_num[i]) * (2 ** (len(bin_num) - 1 - i) )

print(f"Decimal value of {bin_num} is {deci_num}")