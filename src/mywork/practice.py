from z3 import *

#Parts
squ = Real('squ')
cir = Real('cir')
tri = Real('tri')

#Constraints
C1 = squ + cir + tri == 10
C2 = cir + squ - tri == 6
C3 = cir + tri - squ == 4

C = And(C1, C2, C3)

s = Solver()
s.add(C)

isSat = s.check()
if(isSat == sat):
    print(s.model())
else:
    print("-1")