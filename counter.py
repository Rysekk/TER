def countTrueClause(tabRep):
    countTrue = 0
    for i in range(len(tabRep)):
        if(tabRep[i]):
            countTrue += 1
    return countTrue




def getIndex(list, el):
    for i in range(len(list)):
        if(list[i] == el):
            return i


def countTruePop(pop):
    count = 0
    l = []
    for i in range(len(pop)):
        tc = countTrueClause(pop[i])
        l.append(tc)
    return l