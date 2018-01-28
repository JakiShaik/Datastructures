import random
def _search(tree,e):
	if tree==[]:
		return []
	if e == tree[1]:
		return (tree)
	if e > tree[1]:
		return _search(tree[2],e)
	if e < tree[1]:
		return _search(tree[0],e)
	return []
def search (tree,e):
	if tree==[]:
		print("False")
		return
	if e == tree[1]:
		print ("True")
		return
	if e > tree[1]:
		return search(tree[2],e)
	if e < tree[1]:
		return search(tree[0],e)
	print("False")
	return
def sh(tree,el):
	if tree==[]:
		return
	else:
		sh(tree[0],el)
		el.append(tree[1])
		sh(tree[2],el)
	return(el)
def sorted(tree):
	el=[]
	return sh(tree,el)
def insert(tree,i):
	f = sorted(tree)
	f.append(i)
	print (f)
	return sort(f)
def sort(a):
	if a==[]:
		return []
	else:
		pivot=random.choice(a)
		a.remove(pivot)
		left=[x for x in a[:] if x <= pivot]
		right=[x for x in a[:] if x > pivot]
		return [sort(left)] + [pivot] + [sort(right)]
