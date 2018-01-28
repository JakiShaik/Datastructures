def hgt(a):
    if a == []:
        return 0
    if a[0] == [] and a[2] == []:
        return 0
    l = hgt(a[0])
    r = hgt(a[2])
    return 1 + max(l,r)
a = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]
print(hgt(a))