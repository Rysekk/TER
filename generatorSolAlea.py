from random import randint

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

def genTabSolAlea(nbSol, tailleSol):
    tabSol = []
    for i in range(nbSol):
        tab = genSolAlea(tailleSol)
        tabSol.append(tab)
    return tabSol 