from itertools import product

if __name__ == '__main__':
    input_list1 = map(int, input().split())
    input_list2 = map(int, input().split())
    print(*product(input_list1,input_list2))
