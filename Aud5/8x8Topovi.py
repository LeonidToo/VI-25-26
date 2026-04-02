from constraint import *

def notSameRow(r1,r2):
    return r1!=r2
problem=Problem()
domains=[s for s in range(8)]
variables=["R1","R2","R3","R4","R5","R6","R7","R8"]
problem.addVariables(variables,domains)
# problem.addConstraint(lambda r1,r2:r1[0]!=r2[0] and r1[1]!=r2[1],variables)
pairs=[]
for var in variables:
    for var1 in variables:
        if var!=var1:
            if not (var1,var) in pairs:
                pairs+=[(var,var1)]
# print(pairs)
for pair in pairs:
    problem.addConstraint(notSameRow,pair)
print(problem.getSolution())