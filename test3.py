import pysat
from pysat.formula import CNF
from pysat.examples.rc2 import RC2Stratified
from pysat.solvers import Lingeling
from random import randint
from operator import index



formula = CNF(from_file='quinn.cnf')
#s = Solver(name='g4')
"""with Lingeling(bootstrap_with=formula.clauses, with_proof=True) as s:
    print(s.solve())
    print(s.accum_stats())
    print(s.get_model())
    print(s.get_core())
"""





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

def genSolAlea(taille):
    sol = []
    seuil = randint(0,100)
    for i in range(taille):
        prob = randint(0,100)
        if(prob > seuil):
            sol.append(True)
        else:
            sol.append(False)
    return sol

def countTrueClause(tabRep):
    countTrue = 0
    for i in range(len(tabRep)):
        if(tabRep[i]):
            countTrue += 1
    return countTrue

def genTabSolAlea(nbSol, tailleSol):
    tabSol = []
    for i in range(nbSol):
        tab = genSolAlea(tailleSol)
        tabSol.append(tab)
    return tabSol 


def getIndex(list, el):
    for i in range(len(list)):
        if(list[i] == el):
            return i

def selectElite(sols, nbToSelect):
    tabSolVal = []
    tabSolCalc = []
    tabWinner = []
    nbWinner = 0
    best = []
    for i in sols:
        tabVal = valuate(i, formula.clauses)
        tabSolVal.append(tabVal)
        tabCalc = calcExp(tabVal)
        tabSolCalc.append(tabCalc)
    while(nbWinner < nbToSelect): 
        for i in tabSolCalc:
            if(countTrueClause(i) > countTrueClause(best)):
                best = sols[getIndex(tabSolCalc, i)]
        nbWinner+=1
        tabWinner.append(best)
        index = getIndex(sols,best)
        print(index)
        tabSolCalc.remove(tabSolCalc[index])
    return tabWinner

def countTruePop(pop):
    count = 0
    l = []
    for i in range(len(pop)):
        tc = countTrueClause(pop[i])
        l.append(tc)
    return l

def valuateTab(tabValuate):
    tab = []
    for i in tabValuate:
        tab.append(valuate(i, formula.clauses))
    return tab

def calcExpTab(tabVal):
    tab = []
    for i in tabVal:
        tab.append(calcExp(i))
    return tab



    
vect = [True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True]
tabRep = valuate(vect, formula.clauses)
#print(tabRep)
tabfiak = calcExp(tabRep)
#print(tabfiak)

tabtest = genSolAlea(16)
print(tabtest)
sols = genTabSolAlea(1, 16)
print(sols)
print(formula.clauses)
elite = selectElite(sols, 1)
print("///////////////////////////////////////////")
print(elite)
tabVal = valuateTab(elite)
print(tabVal)
tabcalc = calcExpTab(tabVal)
print(countTruePop(tabcalc))