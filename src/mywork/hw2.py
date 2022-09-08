from z3 import *
def hw2():
    s = Solver()
    X, Y, Z = Bools('X Y Z')
    
    #X ∨ Y, X ⊢ ¬Y
    #((X \or Y) \and X) \implies \notY
    C1 = Implies(And((Or(X, Y), X)), Not(Y))
    
    
    
    s.add(Not(C1))
    #I believe it's not valid
    
    r = s.check(C1)
    
    if(r == unsat):
        print("C1 is valid")
    else:
        print("Here's a counter example ", s.model())
        
hw2()