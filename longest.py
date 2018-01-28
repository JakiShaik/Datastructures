def longest(a):
    llp,hp = _longest(a)
    return llp
def _longest(a):
    if a == [] or (a[0] == [] and a[2] == []):
        return 0,0
    llength,lhgt = _longest(a[0])
    rlength,rhgt = _longest(a[2])

    if a[0] == [] or a[2] == []:
        lp = max(1+lhgt+rhgt,llength,rlength)
        h = 1 + max(lhgt, rhgt)
    else:
        lp = max(2+lhgt+rhgt,llength,rlength)
        h = 1 + max(lhgt, rhgt)
    return lp,h

a = [ [], 4, [[], 6, [[], 7, [[], 9, [[],10,[]]]]]]
print(longest(a))

