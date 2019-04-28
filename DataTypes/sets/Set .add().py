# s = set('HackerRank')
# print(s)
# s.add('H')
# print(s)
# print(s.add('HackerRank'))
# print(s)

n = int(input())
s = set()
for i in range(0, n):
    s.add(input())
print(s.__len__())