from pip._vendor.distlib.compat import raw_input

i = int(input())
lis = list(map(int, input().split()))
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(max(lis))