from random import randint
def qselect(index, list):
    if list == [] or index<1:
        return None
    else:
        rand = randint(0,len(list)-1) #generates a random element from the list
        pivot = list[rand] #rand index is set to pivot
        #list.remove(rand)
        left = [x for x in list if x< pivot]
        right = [x for x in list if x> pivot]
        mid = [x for x in list if x == pivot]
        if(index <= len(left)):
            return qselect(index,left)
        elif(index < len(left)+len(mid)+1):
            return pivot
        else:
            return qselect(index-len(left)-len(mid),right)

print(qselect(4, [11, 2, 8, 3]))
