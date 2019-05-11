import re
if __name__ == '__main__':
    t = int(input())
    expressions = []
    for i in range (0, t):
        expressions[i].insert(input())
    for i in range (0, t):
        m = re.compile(expressions[i])
        if m:
            print("True")
        else:
            print("False")
