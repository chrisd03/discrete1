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
        
    #X ↔ Y ⊢ Y → X
    #(X biimplies Y) implies (Y implies X)
    #If X is equivalent to Y then if Y is true X is true
    C12 = Implies(X == Y, Implies(Y, X))
    s.reset()
    s.add(Not(C12))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C12 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    
    #X ∨ Y, X → Z, Y → Z ⊢ Z
    #((X or Y) and (X implies Z) and (Y implies Z)) implies Z
    #If X is true or Y is true, and Z is true if X is true, and Z is true if Y is true then Z is true
    C13 = Implies(And(Or(X, Y), Implies(X, Z), Implies(Y, Z)), Z)
    s.reset()
    s.add(Not(C13))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C13 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    
    #X → Y, Y ⊢ X  
    #((X implies Y) and Y) implies X 
    #If Y is true when X is true, and Y is true then X must be true
    C14 = Implies(And(Implies(X, Y), Y), X)
    s.reset()
    s.add(Not(C14))
    #I believe it's not valid
    r = s.check()
    if(r == unsat):
        print("C14 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    
    #X → Y, X ⊢ Y
    #((X implies Y) and X) implies Y 
    #If Y is true when X is true, and X is true then X must be true
    C15 = Implies(And(Implies(X, Y), X), Y)
    s.reset()
    s.add(Not(C15))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C15 is valid")
    else:
        print("Here's a counter example", s.model())     
    
    
    #X → Y, Y → Z ⊢ X → Z
    #((X implies Y) and (Y implies Z)) implies (X implies Z)
    #If Y is true when X is true, and Z is true when Y is true then Z must be true when X is true
    C16 = Implies(And(Implies(X, Y), Implies(Y, Z)), Implies(X, Z))
    s.reset()
    s.add(Not(C16))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C16 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    #X → Y ⊢ Y → X
    #(X implies Y) implies (Y implies X)
    #If Y is true when X is true then X is true when Y is true
    C17 = Implies(Implies(X, Y), Implies(Y, X))
    s.reset()
    s.add(Not(C17))
    #I believe it's not valid
    r = s.check()
    if(r == unsat):
        print("C17 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    #X → Y ⊢ ¬Y → ¬X
    #(X implies Y) implies (Not(Y) implies (Not(X))
    #If Y is true when X is true then when Y is false X is false
    C18 = Implies(Implies(X, Y),Implies(Not(Y), Not(X)))
    s.reset()
    s.add(Not(C18))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C18 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    #¬(X ∨ Y) ↔ ¬X ∧ ¬Y
    #Not(X or Y) biimplies Not(X) and Not(Y)
    #X or Y being false is equivalent to X and Y both being false
    C19 = Not(Or(X, Y)) == And(Not(X), Not(Y))
    s.reset()
    s.add(Not(C19))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C19 is valid")
    else:
        print("Here's a counter example", s.model()) 
        
    
    #¬(X ∧ Y) ↔ ¬X ∨ ¬Y
    #Not(X and Y) biimplies Not(X) or Not(Y)
    #X and Y being false is equivalent to X being false or Y being false
    C20 = Not(And(X, Y)) == Or(Not(X), Not(Y))
    s.reset()
    s.add(Not(C20))
    #I believe it's valid
    r = s.check()
    if(r == unsat):
        print("C20 is valid")
    else:
        print("Here's a counter example", s.model())
hw2()