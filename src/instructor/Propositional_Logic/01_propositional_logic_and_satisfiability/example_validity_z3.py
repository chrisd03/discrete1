from z3 import *

def isValid(P) : #P -> proposition
    s = Solver()
    s.add(Not(P)) #If not P is unsat then P is valid <----------. Can't do sat bc sat doesn't imply validity
    return (s.check()==unsat)

# Declare X to be a Z3 Bool variable
X = Bool('X')
# Print the result of testing (X Or Not X) for validity
print(isValid(Or(X, Not(X)))) #always valid. 
# Print the result of testing (X And Not X) for validity
print(isValid(And(X, Not(X))))#unsatisfiable


#unsat(!P) <-> valid(P)