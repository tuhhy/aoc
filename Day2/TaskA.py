lst = []
with open('input.txt') as f:
    lst = f.readlines()

lststrip = []
for i in lst:
    lststrip.append(i.strip())
print(lststrip)

newlist = []
score = 0

for i in lststrip:
    if i[0] == 'A' and i[2] == 'Y':
        score += 6
    elif i[0] == 'B' and i[2] == 'Z':
        score += 6
    elif i[0] == 'C' and i[2] == 'X':
        score += 6

    elif i[0] == 'A' and i[2] == 'X':
        score += 3
    elif i[0] == 'B' and i[2] == 'Y':
        score += 3
    elif i[0] == 'C' and i[2] == 'Z':
        score += 3

    if i[2] == 'X':
        score += 1
    elif i[2] == 'Y':
        score += 2
    elif i[2] == 'Z':
        score += 3

    print(i[0], i[2])
    print(score)
    newlist.append(score)
print(sum(newlist))