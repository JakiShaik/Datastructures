from collections import defaultdict


#For a bag weight X we will calculate how many ith items we can put and then i+1th and so on. Like this we will check all the possible combinations
# and fill all the values in the table. We will calculate maximum value out of that
def best(w,items):
    n = len(items)
    back = defaultdict(int)

    def _best(x,i,opt=defaultdict(int)):
        if i<0 or (x,i) in opt:
            print('in return i is '+str(i))
            print('in return')
            return opt[x,i]
        w,v,c = items[i]
        xx = x
        print('c is '+str(c))
        for j in range(0,c+1):
            if xx<0:
                break
            ans = _best(xx,i-1) + v * j #Here we are reducing the items number till it goes to 0 and when the items is less than zero line number 11
            # will jus return 0. After all the recursions and j loop starts to run XX which is the weight of the bag will be reduced by weight of this
            #particular item and best will be called upon this size of the bag and for a smaller item
            print('j is '+str(j))
            print('i is'+str(i))
            print(ans)
            print(opt)
            if ans > opt[x, i]:
                opt[x, i] = ans
                back[x, i] = j
            xx -= w # Here we are reducing the weight of the bag
        return opt[x, i]

    return _best(w, n - 1)
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))