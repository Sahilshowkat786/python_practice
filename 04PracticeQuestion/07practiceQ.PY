nos = [0, 1, 0, 3, 12, 11, 56, 0, 17]

for i in nos:
    if i == 0:
        nos.remove(i)
        nos.append(0)

print(nos)