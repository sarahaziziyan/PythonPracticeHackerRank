import string

if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(0, N):
        command = input()
        cm = command.split(' ')
        if command.__contains__("insert"):
            L.insert(int(cm[1]), int(cm[2]))
        if command.__contains__("remove"):
            L.remove(int(cm[1]))
        if command.__contains__("append"):
            L.append(int(cm[1]))
        if command.__contains__("sort"):
            L.sort()
        if command.__contains__("reverse"):
            L.reverse()
        if command.__contains__("pop"):
            L.pop()
        if command.__contains__("print"):
            print(L)
