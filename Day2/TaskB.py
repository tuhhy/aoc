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
    if i[0] == 'A':
        if i[2] == 'X':
            score += 3
        if i[2] == 'Y':
            score += 1
        if i[2] == 'Z':
            score += 2
    if i[0] == 'B':
        if i[2] == 'X':
            score += 1
        if i[2] == 'Y':
            score += 2
        if i[2] == 'Z':
            score += 3
    if i[0] == 'C':
        if i[2] == 'X':
            score += 2
        if i[2] == 'Y':
            score += 3
        if i[2] == 'Z':
            score += 1

    if i[2] == 'X':
        score += 0
    elif i[2] == 'Y':
        score += 3
    elif i[2] == 'Z':
        score += 6

    print(i[0], i[2])
    print(score)
    newlist.append(score)