import pysat
from pysat.formula import WCNF
from pysat.examples.rc2 import RC2Stratified
formula = WCNF(from_file='instance1.wcnf')

rc2g4 = RC2Stratified(formula,solver="g4")
rc2g4 = RC2Stratified(formula,solver="g4")
model = rc2.compute()
print("model = ",model)
print("cost = ",rc2.cost)