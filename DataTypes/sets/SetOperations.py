n = int(input())
englishSet = set(map(int, input().split()))
m = int(input())
frenchhSet = set(map(int, input().split()))

union = englishSet.union(frenchhSet)
intersection = englishSet.intersection(frenchhSet)
difference = englishSet.difference(frenchhSet)
symmetric_difference = englishSet.symmetric_difference(frenchhSet)
print(englishSet)
print(frenchhSet)

print(union)
print(union.__len__())

print(intersection)
print(intersection.__len__())

print(difference)
print(difference.__len__())

print(symmetric_difference)
print(symmetric_difference.__len__())

