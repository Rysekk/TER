import random


def genRandomBool():
    rand = random.random()
    if(rand < 0.5 ):
        return True
    else:
        return False

def selectRandBool(tabBool):
    i = random.randint(0,len(tabBool) - 1)
    return tabBool[i]



def genExp(nbClause, nbVar, maxVarClause):
    tabVar = []
    tabClause = []

    for i in range(nbVar):
        bool = "x"+str(i)
        tabVar.append(bool)

    for i in range(nbClause):
        nbMaxCl = random.randint(1, maxVarClause)
        clause = []
        for j in range(nbMaxCl):
            if(random.random() > 0.5):
                clause.append(selectRandBool(tabVar))
            else:
                clause.append("not "+selectRandBool(tabVar))
        tabClause.append(clause)

    return tabClause


def valuate(exp, tabVal):
    for k in range (len(tabVal)):
        for i in range (len(exp)):
            for j in range(len(exp[i])):
                if(exp[i][j] == "x"+str(k)):
                    exp[i][j] = tabVal[k]
                elif(exp[i][j] == "not x"+str(k)):
                    exp[i][j] = not tabVal[k]

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

def countTFClause(tabRep):
    countTrue = 0
    countFalse = 0
    tabCount = []
    for i in range(len(tabRep)):
        if(tabRep[i] == True):
            countTrue += 1
        else:
            countFalse += 1
    tabCount.append("nombre de clauses true : "+str(countTrue))
    tabCount.append("nombre de clauses false : "+str(countFalse))
    return tabCount





tabVal = [True, False, True , True,False]
exp = genExp(500,100,3) #nbClause, nbVar, maxVarClause
print(exp)

valuate(exp, tabVal)
print(exp)
tabRep = calcExp(exp)
print(tabRep)
print(countTFClause(tabRep))





