#!/bin/python3

import math
import os
import random
import re
import sys

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


# Complete the solve function below.
def solve(s):
    splited = s.split(" ")
    for i in range(0, len(splited)):
        splited[i] = mutate_string(splited[i],0,splited[i][0].upper())

    return ' '.join(splited)

if __name__ == '__main__':
    s = input()
    print(solve(s))