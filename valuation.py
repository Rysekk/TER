

def valuate(vect, exp):
    tabRep = [[]]
    for i in range (len(exp)):
        if(i < len(exp) - 1 ):
            tabRep.append([])
        for j in range(len(exp[i])):
            tabRep[i].append(True)

    for k in range (len(vect)):
        for i in range (len(exp)):
            for j in range(len(exp[i])):
                if(exp[i][j] == k+1):
                    tabRep[i][j] = vect[k]
                elif(exp[i][j] == -(k+1)):
                    tabRep[i][j] = not vect[k]
    return tabRep



def valuateTab(tabValuate, exp):
    tab = []
    for i in tabValuate:
        tab.append(valuate(i, exp.clauses))
    return tab