def numJewelsInStones(J, S):
    jSet = set(J)
    print(jSet)
    return sum(s in jSet for s in S)


J = "aA"
S = "aAAbbbb"
x = numJewelsInStones(J, S)
print(x)