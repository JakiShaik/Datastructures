def _num_yes(n,yes):
    if n in yes:
        return yes[n]
    else:
        yes[n] = _num_yes(n-1,yes) + _num_yes(n-2,yes) + pow(2,n-2)
    return yes[n]
def num_yes(n):
    yes = {0:0,1:0}
    return _num_yes(n,yes)
print(num_yes(3))
def num_no(n):
    yes = {0:0,1:0}
    num_yes = _num_yes(n,yes)
    return pow(2,n) - num_yes
print(num_no(3))
