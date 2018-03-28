import collections
import math
def tsp(nodes,vector):
	len=list(range(nodes))
	distance=[[math.inf for i in range(nodes)] for j in range(nodes)]
	for i in vector:
		s,d,w=i
		distance[s][d]=w
		distance[d][s]=w
	return _tsp(len,distance)
def _tsp(lenth,distance):
	def solution(l,k):
		if not l:
			return [k]
		else:
			l.remove(k)
			return [k]+solution(l,c[frozenset(l),k][1])
	t=lenth[1:]
	pos=0
	ll=[]
	result=[0]
	while pos<len(t):
		for i in range(len(t)):
			te=t[::]
			te.remove(t[i])
			for j in range(len(te)+1-pos):
				ss=frozenset(te[j:pos+1]),t[i]
				if ss not in ll:
					ll.append(ss)
		pos+=1
	c={}
	for i in sorted(ll):
		if not i[0]:
			c[i]=[distance[i[1]][0],0]
		else:
			t1=list(i[0])
			v=i[1]
			if len(t1)<=1:
				x,*_=i[0]
				t1.remove(x)
				c[i]=[distance[i[1]][x]+c[frozenset(t1),x][0],x]
			else:
				minv=math.inf
				p=None
				for iter in i[0]:
					t2=t1[::]
					t2.remove(iter)
					if distance[v][iter]+c[frozenset(t2),iter][0]<minv:
						minv=distance[v][iter]+c[frozenset(t2),iter][0]
						p=iter
				c[i]=[minv,p]
	minv=math.inf
	p=None
	ft=frozenset(t)
	for i in ft:
		t2=t[::]
		t2.remove(i)
		if distance[0][i]+c[frozenset(t2),i][0]<minv:
			minv=distance[0][i]+c[frozenset(t2),i][0]
			p=i
	c[ft,0]=[minv,p]
	return c[ft,0][0],[0]+solution(t,c[ft,0][1])
print(tsp(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
print(tsp(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (3,0,1)]))
print(tsp(11, [(0,1,29),(0,2,20),(0,3,21),(0,4,16),(0,5,31),(0,6,100),(0,7,12),(0,8,4),(0,9,31),(0,10,18),
                (1,2,15),(1,3,29),(1,4,28),(1,5,40),(1,6,72),(1,7,21),(1,8,29),(1,9,41),(1,10,12),
                (2,3,15),(2,4,14),(2,5,25),(2,6,81),(2,7,9),(2,8,23),(2,9,27),(2,10,13),
                (3,4,4),(3,5,12),(3,6,92),(3,7,12),(3,8,25),(3,9,13),(3,10,25),
                (4,5,16),(4,6,94),(4,7,9),(4,8,20),(4,9,16),(4,10,22),
                (5,6,95),(5,7,24),(5,8,36),(5,9,3),(5,10,37),
                (6,7,90),(6,8,101),(6,9,99),(6,10,84),
                (7,8,15),(7,9,25),(7,10,13),
                (8,9,35),(8,10,18),
                (9,10,38)]))