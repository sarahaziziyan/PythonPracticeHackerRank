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
    inSpaceChar = True
    for i in range(0, len(s)):
        if(s[i].__eq__(' ')):
            inSpaceChar = True
        else:
            if(inSpaceChar):
                s = mutate_string(s,i,s[i].upper())
                inSpaceChar = False

    return s

if __name__ == '__main__':
    s = input()
    print(solve(s))