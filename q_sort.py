def q(l):
    if len(l) <= 1:
        return l
    return q([a for a in l[1:] if a < l[0]]) + l[0:1] + q([b for b in l[1:] if b >= l[0]])


ab = [2, 7, 1, 6, 4, 9, 8, 3, 5]
print(q(ab))
