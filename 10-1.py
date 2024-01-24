numbs = []
c = False
a = int(input())
for i in range(a):
    numbs.append(int(input()))
keynum = int(input())
for i in range(a - 1):
    for j in range(i + 1, a):
        if numbs[i] * numbs[j] == keynum:
            c = True
            break
if c:
    print('ДА')
else:
    print('НЕТ')