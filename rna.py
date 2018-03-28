from collections import defaultdict
# def best(seq):
#     def _best(seq):
#         j=len(seq)
#         c4 = 0
#         i = 0
#         if j == 0:
#             return 0
#         if j == 1:
#             return 0
#         if seq in d:
#             return d[seq]
#         for k in range(1,j):
#             if seq[i] + seq[k] in match:
#                 d[seq[i+1:k]] = c2 = _best(seq[i+1:k])
#                 d[seq[k+1:j]] = c3 = _best(seq[k+1:j])
#                 c4 = c2 + c3 + 1
#         d[seq[1:]] = c1 = _best(seq[1:])
#         d[seq] = max(c1,c4)
#         return d[seq]
#
#     d={}
#     match = ["AU", "GC", "GU", "UG", "CG", "UA"]
#     return _best(seq)
#
# print(best("ACAGU"))

def best(s):
    nl = ['AU', 'GC', 'GU', 'UA', 'CG', 'UG']
    d = {}

    def _best(s):
        c, b = 0, ''
        j = len(s)
        if j == 0:
            return 0, ''
        elif j == 1:
            return 0, '.'
        if s in d:
            return d[s]
        for k in range(1, j):
            if s[0] + s[k] in nl:
                d[s[1:k]] = (c1, b1) = _best(s[1:k])
                d[s[k + 1:j]] = (c2, b2) = _best(s[k + 1:j])
                if (c1 + c2 + 1) > c:
                    c = c1 + c2 + 1
                    b = '(' + b1 + ')' + b2
        d[s[1:]] = (c3, b3) = _best(s[1:])
        b3 = '.' + b3
        d[s] = (c, b) if c > c3 else (c3, b3)
        return d[s]

    return _best(s)


def total(s):
    d = {}
    nl = ['AU', 'GC', 'GU', 'UA', 'CG', 'UG']

    def _total(s):
        t = 0
        j = len(s)
        if j == 0:
            return 1
        elif j == 1:
            return 1
        if s in d:
            return d[s]
        for k in range(1, j):
            if s[0] + s[k] in nl:
                d[s[1:k]] = t1 = _total(s[1:k])
                d[s[k + 1:j]] = t2 = _total(s[k + 1:j])
                t += (t1 * t2)
        d[s[1:]] = t3 = _total(s[1:])
        t += t3
        d[s] = t
        return d[s]

    return _total(s)
def kbest(s,k=10):
    nl = ['AU', 'GC', 'GU', 'UA', 'CG', 'UG']
    d = {}
    res = []

    def _best(s):
        c, b = 0, ''
        j = len(s)
        if j == 0:
            return 0, ''
        elif j == 1:
            return 0, '.'
        if s in d:
            return d[s]
        for l in range(1, j):
            if s[0] + s[l] in nl:
                d[s[1:l]] = (c1, b1) = _best(s[1:l])
                d[s[l + 1:j]] = (c2, b2) = _best(s[l + 1:j])
                c = c1 + c2 + 1
                b = '(' + b1 + ')' + b2
                if(len(b) == j):
                    res.append((c,b))
        d[s[1:]] = (c3, b3) = _best(s[1:])
        b3 = '.' + b3
        if(len(b3)==j):
            res.append(b3)
        d[s] = (c, b) if c > c3 else (c3, b3)
        #print(d)
        print(res)
        return d[s]

    return _best(s)

kbest('ACAGU')