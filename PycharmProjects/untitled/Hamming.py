def hammingDistance(x, y):
    """
    :type J: str
    :type S: str
    :rtype: int
    """

    o = []
    for i, j in zip(list(format(x, '032b')), list(format(y, '032b'))):
        o.append(1) if (j!= i) else o.append(0)
    return sum(o)





p = hammingDistance(1, 300)
print(p)
format(2, '08b')