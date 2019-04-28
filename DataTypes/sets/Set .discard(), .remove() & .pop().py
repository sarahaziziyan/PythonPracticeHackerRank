
n = int(input())
s = set(map(int, input().split()))

commandNo = int(input())
for i in range(0, commandNo):
    command = input()
    cm = command.split()
    if command.__contains__("pop"):
        s.pop()
    if command.__contains__("remove"):
        s.remove(int(cm[1]))
    if command.__contains__("discard"):
        s.discard(int(cm[1]))

sum = 0
for i in s:
    sum += i

print(sum)