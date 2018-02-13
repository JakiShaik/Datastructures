def bsts(n):
    bsts = [1]
    return _bsts(n,bsts)
def _bsts(n,bsts):
    for i in range(1,n+1):
        sum = 0
        for j in range(1,i+1):
            sum += bsts[j-1]*bsts[i-j]
        bsts.append(sum)
    return bsts[n]
print(bsts(5))
