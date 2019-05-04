def print_formatted(number):
    # for i in range(0,number):
    #     #print(i,hex(i),oct(i),bin(i))
    #     w = len(bin(i)[2:])
    #     print(w)
    #
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#'{:>10}'.format('test') align right
#'{:10}'.format('test') align left