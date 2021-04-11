

def calcExp(exp):
    tabRep = []
    for i in range (len(exp)):
        for j in range (len(exp[i])):
            if(exp[i][j] == True):
                for k in range (len(exp[i])):
                    exp[i][k] = True
    for i in range(len(exp)):
        if(exp[i][0] == True):
            tabRep.append(True)
        else:
            tabRep.append(False)
    return tabRep

def calcExpTab(tabVal):
    tab = []
    for i in tabVal:
        tab.append(calcExp(i))
    return tab
