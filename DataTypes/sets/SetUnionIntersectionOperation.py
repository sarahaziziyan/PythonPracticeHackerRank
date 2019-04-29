n = int(input())
englishSet = set(map(int, input().split()))
m = int(input())
frenchhSet = set(map(int, input().split()))

union = englishSet.union(frenchhSet)
intersection = englishSet.intersection(frenchhSet)
print(englishSet)
print(frenchhSet)
print(union)
print(intersection)
print(union.__len__())
print(intersection.__len__())

