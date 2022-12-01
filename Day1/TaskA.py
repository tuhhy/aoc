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
print(max(maxint))
