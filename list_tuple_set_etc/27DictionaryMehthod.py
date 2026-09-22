ep1={
    122:23,
    123:78,
    238:12,
    199:15
}
ep2={
    222:33,
    566:90
}
ep1.update(ep2)
print(ep1)
ep1.pop(238)
print(ep1)
ep1.popitem()  #remove last element
print(ep1)
ep1.clear()
print(ep1)
del ep2[222]
print(ep2)