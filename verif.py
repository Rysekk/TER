import pysat
from pysat.formula import CNF
from pysat.examples.rc2 import RC2Stratified
from pysat.solvers import Lingeling
from random import randint
from operator import index
from pysat.solvers import Lingeling





formula = CNF(from_file='gros.cnf')
#s = Solver(name='g4')
"""with Lingeling(bootstrap_with=formula.clauses, with_proof=True) as s:
    print(s.solve())
    print(s.accum_stats())
    print(s.get_model())
    print(s.get_core())
    print(s.get_proof())"""