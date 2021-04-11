from valuation import valuate, valuateTab
from calculeExp import calcExp, calcExpTab
from counter import countTrueClause, getIndex, countTruePop
 



def selectElite(sols, nbToSelect, formula):
    tabVal = valuateTab(sols, formula)
    tabRep = calcExpTab(tabVal) 
    tabC = countTruePop(tabRep)
    tabWinner = []
    nbselected = 0
    best = 0
    print(sols)
    print(tabC)
    while(nbselected < nbToSelect):
        for i in range(len(tabC)):
            if(tabC[i] > best):
                best = tabC[i]
                idbest = i
        print("best", best)
        print("idbest", idbest)
        print("tabC[idbest]", tabC[idbest])
        nbselected+=1
        tabWinner.append(sols[idbest])
        tabC[idbest] = 0
        best = 0
        idbest = 0
        
    return tabWinner
