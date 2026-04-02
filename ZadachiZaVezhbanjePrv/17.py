from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(),variables)
    def constraint_2(B,D,E):
        return B%2!=0 and D%2!=0 and E%2!=0
    problem.addConstraint(constraint_2,["B","D","E"])
    def constraint_3(a,b,c):
        return (a+b+c)>99
    problem.addConstraint(constraint_3,["A","B","C"])
    problem.addConstraint(lambda d,e:d+e==150,["D","E"])
    problem.addConstraint(lambda f:f%10%4==0,"F")
    # ----------------------------------------------------

    print(problem.getSolution())