n = int(input())
englishSet = set(map(int, input().split()))
m = int(input())
frenchhSet = set(map(int, input().split()))

union = englishSet.union(frenchhSet)
print(englishSet)
print(frenchhSet)
print(union)
print(union.__len__())

