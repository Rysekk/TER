import pysat
from pysat.formula import CNF
from pysat.examples.rc2 import RC2Stratified
from pysat.solvers import Lingeling
from random import randint, random
from operator import index
import valuation, calculeExp, generatorSolAlea, selection, verif, counter
 



formula = CNF(from_file='quinn.cnf') #petitgros 168 clauses et 100 variables 

def getChild(vect1, vect2):        #fait un enfant entre deux vecteurs de valuation on prenant un morceau de l'un et en ajoutant le morceau de l'autre après
    rand = randint(0, len(vect1))
    vect3 = []
    for i in range(len(vect1)):
        if(i < rand): 
            vect3.append(vect1[i]) 
        else:
            vect3.append(vect2[i])
    return vect3

def extendPop(sols, prob):              #prend chaque individu et lui affecte un partenaire selon une proba, ils produisent un enfant avec getChild()
    for i in range(len(sols)):
        idpartner = randint(0, len(sols) - 1)
        probGetChild = random()
        probInversed = random()
        if(probGetChild < prob and not probInversed):
            sols.append(getChild(sols[i], sols[idpartner]))
        elif(probGetChild < prob and probInversed):
            sols.append(getChild(sols[idpartner], sols[i]))
    return sols



nbVar = 16
"""
vect = [True,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True]
tabRep = valuation.valuate(vect, formula.clauses)
#print(tabRep)
tabfiak = calculeExp.calcExp(tabRep)
#print(tabfiak)"""


sols = generatorSolAlea.genTabSolAlea(10, nbVar)
tabVal = valuation.valuateTab(sols, formula)
tabcalc = calculeExp.calcExpTab(tabVal)
print(counter.countTruePop(tabcalc))  

elite = selection.selectElite(sols, 3, formula)
tabVal = valuation.valuateTab(elite, formula)
tabcalc = calculeExp.calcExpTab(tabVal)
print(counter.countTruePop(tabcalc))

solwchild = extendPop(elite, 0.3)
tabVal = valuation.valuateTab(solwchild, formula)
tabcalc = calculeExp.calcExpTab(tabVal)
print(counter.countTruePop(tabcalc))  

print("///////////////////////////////////////")
"""tabVal = valuation.valuateTab(sols, formula)
tabcalc = calculeExp.calcExpTab(tabVal)
print(counter.countTruePop(tabcalc))
print("///////////////////////////////////////")
print(formula.clauses)
elite = selection.selectElite(sols, 5, formula)

print("///////////////////////////////////////////")

print(elite)
print("///////////////////////////////////////////")
tabVal = valuation.valuateTab(elite, formula)
print(tabVal)
print("///////////////////////////////////////////")
tabcalc = calculeExp.calcExpTab(tabVal)
print(tabcalc)
print("////////////////////////////")
print(counter.countTruePop(tabcalc))"""