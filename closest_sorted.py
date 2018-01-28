import bisect
def find(a,num,k):
    if a == [] or k <1:
        return None
    index = bisect.bisect_left(a,num)
    i = j = index
    count = 0
    output = []
    i = i-1
    while(k > count):
        if(i > 0 and j < len(a)):
            if (abs(a[i] - num) <= abs(a[j] - num)):
                #output.append(a[i])
                i = i - 1
                count = count+1
            else:
                #output.append(a[j])
                j = j + 1
                count = count +1
        elif(i >=0 and j == len(a)):
            i = i-1
            count = count +1
        elif(i == 0 and j < len(a)):
            j= j+1
            count = count +1
    output = a[i+1:j]
    return output
    #print(output)

find([1,2,3,4,4,7], 6.5, 3)