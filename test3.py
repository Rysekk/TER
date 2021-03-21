import pysat
from pysat.formula import CNF
from pysat.examples.rc2 import RC2Stratified
formula = CNF(from_file='quinn.cnf')
print(formula.clauses[1])
"""
rc2g4 = RC2Stratified(formula,solver="g4")
rc2g4 = RC2Stratified(formula,solver="g4")
model = rc2.compute()
print("model = ",model)
print("cost = ",rc2.cost)"""