#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
import time
import random

count = 2

while True:
    #random.random() creates a random value between 0 and 1
    print("2")
    delay = random.random() + 2
    count = count + 2
    if count > 20:
        break