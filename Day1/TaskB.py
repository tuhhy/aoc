from operator import indexOf

lst = []
with open('input.txt') as f:
    lst = f.readlines()
print(lst)

maxint = []
group = 0
for i in lst:
    if i.strip() == '':
        maxint.append(group)
        group = 0
    else:
        group += int(i.strip())

wirklichmax = []
for i in range(3):
    wirklichmax.append(maxint.pop(indexOf(maxint, max(maxint))))
print(wirklichmax)
print(sum(wirklichmax))