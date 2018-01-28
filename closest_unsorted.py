from random import randint
def qselect(diff,n):
    rand = randint(0, len(diff) - 1)
    pivot = diff[rand]
    left = [x for x in diff if x[0] < pivot[0]]
    mid = [x for x in diff if x[0] == pivot[0]]
    right = [x for x in diff if x[0]> pivot[0]]
    if(n <= len(left)):
        return qselect(left,n)
    elif(n < len(left)+len(mid)+1):
        return mid[n-len(left)-1]
    else:
        return qselect(right,n-len(left)-len(mid))
def find(a,k,n):
    if a == []:
        return 0
    diff = []
    for i in range(len(a)):
        diff.append((abs(a[i]-k),a[i],i))
    result = []
    for i in range(1,n+1):
        result.append(qselect(diff,i))
    #output = []
    for j in range(len(result)):
        for k in range(len(result)):
            if(result[j][2] < result[k][2]):
                result[j],result[k] = result[k],result[j]
    for i in result:
        #output.append(i[1])
        print(i[1])
    #print(output)

find([4,1,3,2,7,4], 6.5, 3)
