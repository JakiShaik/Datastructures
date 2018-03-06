from collections import defaultdict
def longest(num_nodes,vector):
    def order(num_nodes, vector):
        adjlist = []
        degree = []
        res = []
        for i in range(num_nodes):
            adjlist.append([])
            degree.append(0)
        for tupl in vector:
            adjlist[tupl[0]].append(tupl[1])
            degree[tupl[1]] += 1
        degree1 = degree[:]
        for i in range(num_nodes):
            if degree[i] == 0:
                res.append(i)
        for node in res:
            for sucnode in adjlist[node]:
                degree[sucnode] -= 1
                if degree[sucnode] == 0:
                    res.append(sucnode)
        if max(degree) == 0:
            return res, adjlist
        else:
            return None, adjlist

    topsort, adjlist = order(num_nodes, vector)
    lengthdic = defaultdict(int)
    listdic = defaultdict(list)
    for node in topsort:
        for connnode in adjlist[node]:
            lengthdic[connnode] = lengthdic[node] + 1
            listdic[connnode].append(node)
    # print(dic1)
    resultlen = max(lengthdic.values())
    k = max(lengthdic, key=lengthdic.get)
    result = []
    result.append(k)

    def res(k):
        reqlngth = 0
        for node in listdic[k]:
            lngth, reqnode = lengthdic[node], node
            if (lngth > reqlngth):
                reqlngth = lngth
                reqnode = node
        result.append(reqnode)
        if (lengthdic[reqnode] > 0):
            res(reqnode)
        else:
            return

    res(k)
    result = result[::-1]
    return resultlen, result
print(longest(9, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7),(5,8),(6,7),(8,7)]))
#(5, [0, 2, 3, 4, 5, 6])
print(longest(20000, [(4402, 18651), (2067, 8358), (3863, 16234), (14728, 15474), (6879, 12439), (3075, 15986), (928, 12773), (14180, 19904), (69, 14594), (7496, 8727), (3349, 19370), (1002, 10401), (731, 833), (301, 17741), (7097, 12491), (951, 13831), (7264, 17289), (14348, 16246), (7637, 18116), (7565, 11327), (7169, 15060), (704, 9495), (13637, 18233), (3276, 6091), (3961, 9712), (10901, 16410), (13831, 16636), (6220, 9940), (9311, 19253), (16363, 16557), (12889, 19300), (1131, 15736), (7954, 13247), (5669, 13576), (12029, 17983), (2833, 12278), (14383, 16660), (3536, 5364), (12886, 17070), (12141, 16046), (969, 15378), (1424, 10109), (18945, 19437), (5582, 12897), (5524, 16457), (403, 7436), (6537, 17682), (7607, 17967), (13253, 16835), (11266, 18933), (11576, 15044), (8823, 17956), (187, 19953), (12572, 16793), (4235, 16996), (6733, 18394), (1839, 13962), (11951, 15764), (18166, 18677), (6548, 16538), (13546, 15890), (11691, 13579), (51, 11340), (17644, 17698), (10850, 15012), (916, 19656), (5806, 7523), (18047, 19151), (3001, 5923), (8365, 18056), (1063, 2308), (546, 2727), (477, 14843), (8177, 9214), (3587, 8802), (6049, 11286), (2277, 9512), (5230, 5487), (8362, 17281), (5509, 8942), (9649, 14899), (10551, 16269), (3741, 15524), (774, 10223), (11250, 12666), (6161, 13792), (3563, 8467), (8305, 16715), (6851, 19845), (682, 14144), (585, 7385), (4799, 13019), (1157, 5250), (14603, 16590), (13980, 17848), (7228, 16927), (7313, 14773), (1005, 17167), (12940, 18869), (10526, 13968)]))

