#Chris Domingos uhy9xj
from z3 import *
def hw2():
    X, Y, Z = Bools('X Y Z')
    s = Solver()
    
    #X ∨ Y, X ⊢ ¬Y
    #((X or Y) and X) implies not Y
    #If X or Y is true, and X is true then Y has to be false
    C1 = Implies(And(Or(X, Y), X), Not(Y))
    s.add(Not(C1))
    #I believe it's not valid
    r = s.check()
    if(r == unsat):
        print("C1 is valid")
    else:
        print("Here's a counter example", s.model())
    
    
    #X, Y ⊢ X ∧ Y
    #X and Y implies X and Y
    #If X is true and Y is true then X and Y must be true
    C2 = Implies(And(X, Y), And(X, Y))
    s.reset()
    s.add(Not(C2))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C2 is valid")
    else:
        print("Here's a counter example", s.model())
        
        
    #X ∧ Y ⊢ X
    #X and Y implies X
    #If X and Y is true then X must be true
    C3 = Implies(And(X, Y), X)
    s.reset()
    s.add(Not(C3))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C3 is valid")
    else:
        print("Here's a counter example", s.model())
        
    
    #X ∧ Y ⊢ Y
    #X and Y implies Y
    #If X and Y is true then Y must be true
    C4 = Implies(And(X, Y), Y)
    s.reset()
    s.add(Not(C4))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C4 is valid")
    else:
        print("Here's a counter example", s.model())
        
    #¬¬X ⊢ X
    #Not(Not(X)) implies X
    #If X is Not False it must be True
    C5 = Implies(Not(Not(X)), X)
    s.reset()
    s.add(Not(C5))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C5 is valid")
    else:
        print("Here's a counter example", s.model())
    
    
    #¬(X ∧ ¬X)
    #Not(X and Not(X))
    #The opposite of X and Not(X) is True
    C6 = Not(And(X, Not(X)))
    s.reset()
    s.add(Not(C6))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C6 is valid")
    else:
        print("Here's a counter example", s.model())
        

    #X ⊢ X ∨ Y
    #X implies (X or Y)
    #If X is true then X or Y must be true
    C7 = Implies(X, Or(X, Y))
    s.reset()
    s.add(Not(C7))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C7 is valid")
    else:
        print("Here's a counter example", s.model())
        
    #Y ⊢ X ∨ Y
    #Y implies (X or Y)
    #If Y is true then X or Y must be true
    C8 = Implies(Y, Or(X, Y))
    s.reset()
    s.add(Not(C8))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C8 is valid")
    else:
        print("Here's a counter example", s.model())
        

    #X → Y, ¬X ⊢ ¬ Y
    #((X implies Y) and Not(X)) implies Not(Y)
    #If Y is true when X is true, and X is false, then Y must be false
    C9 = Implies(And(Implies(X, Y), Not(X)), Not(Y))
    s.reset()
    s.add(Not(C9))
    #I believe it's not valid
    r = s.check()
    if(r == unsat):
        print("C9 is valid")
    else:
        print("Here's a counter example", s.model())    
    
    
    #X → Y, Y → X ⊢ X ↔ Y
    #((X implies Y) and (Y implies X)) implies X biimplies Y
    #If Y is true when X is true and X is true when Y is true then X is equivalent to Y
    C10 = Implies(And(Implies(X, Y), Implies(Y, X)), X == Y)
    s.reset()
    s.add(Not(C10))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C10 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    #X ↔ Y ⊢ X → Y
    #(X biimplies Y) implies (X implies Y)
    #If X is equivalent to Y then if X is true Y is true
    C11 = Implies(X == Y, Implies(X, Y))
    s.reset()
    s.add(Not(C11))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C11 is valid")
    else:
        print("Here's a counter example", s.model()) 
hw2()