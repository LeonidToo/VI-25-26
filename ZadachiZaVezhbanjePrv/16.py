from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(),variables)
    problem.addConstraint(lambda s,e,n,d,m,o,r,y:((((s*10+e)*10+n)*10+d)+(((m*10+o)*10+r)*10+e))==((((m*10+o)*10+n)*10+e)*10+y),variables)
    # ----------------------------------------------------

    print(problem.getSolution())