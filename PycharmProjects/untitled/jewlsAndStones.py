
def numJewelsInStones( J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewlsList = list(J)
        stoneList = list(S)
        i = 0
        t= 0
        list2 = []
        while ( i < len(jewlsList)):
            t = 0
            while (t < len(stoneList)):
                if jewlsList[i] == stoneList[t]:
                    list2.append(1)
                t = t + 1
            i = i + 1
        total = sum(list2)
        return list2



J = "z"
S = "ZZ"
x = sum(numJewelsInStones(J, S))
print(x)


