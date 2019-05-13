from itertools import *
from string import *

if __name__ == '__main__':
    input = input().split()
    s = sorted(list(input[0]))
    n = int(input[1])
    perm = sorted(list(permutations(s, n)))
    for p in perm:
        for item in p:
            print("%s" %item, end = '')
        print('')


