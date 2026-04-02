from constraint import *

if __name__ == '__main__':
    solvers = {
        "BacktrackingSolver": BacktrackingSolver(),
        "MinConflictsSolver": MinConflictsSolver(),
        "RecursiveBacktrackingSolver": RecursiveBacktrackingSolver()
    }
    problem=Problem()
    solver=input()
    problem.setSolver(solvers.get(solver))
    variables=[(i,j) for i in range(9) for j in range(9)]
    domain=[i for i in range(1,10)]
    problem.addVariables(variables,domain)
    block1=[(i,j) for i in range(0,3) for j in range(0,3)]
    block2=[(i,j) for i in range(0,3) for j in range(3,6)]
    block3=[(i,j) for i in range(0,3) for j in range(6,9)]
    block4=[(i,j) for i in range(3,6) for j in range(0,3)]
    block5=[(i,j) for i in range(3,6) for j in range(3,6)]
    block6=[(i,j) for i in range(3,6) for j in range(6,9)]
    block7=[(i,j) for i in range(6,9) for j in range(0,3)]
    block8=[(i,j) for i in range(6,9) for j in range(3,6)]
    block9=[(i,j) for i in range(6,9) for j in range(6,9)]
    r=[]
    c=[]
    for i in range(9):
        r=[(i,j) for j in range(9)]
        c=[(j,i) for j in range(9)]
        problem.addConstraint(AllDifferentConstraint(),r)
        problem.addConstraint(AllDifferentConstraint(),c)
    problem.addConstraint(AllDifferentConstraint(),block1)
    problem.addConstraint(AllDifferentConstraint(),block2)
    problem.addConstraint(AllDifferentConstraint(),block3)
    problem.addConstraint(AllDifferentConstraint(),block4)
    problem.addConstraint(AllDifferentConstraint(),block5)
    problem.addConstraint(AllDifferentConstraint(),block6)
    problem.addConstraint(AllDifferentConstraint(),block7)
    problem.addConstraint(AllDifferentConstraint(),block8)
    problem.addConstraint(AllDifferentConstraint(),block9)
    rezultat=problem.getSolution()
    a="{"
    if rezultat:
        for (x,y),assign in rezultat.items():
            if x==0 and y==0:
                a+=f'0: {assign}'
            elif x==8 and y==8:
                a += f', {x * 9 + y}: {assign}'
                a+='}'
            else:
                a+=f', {x*9+y}: {assign}'
        print(a)
    else:
        print("None")



# from constraint import *
#
# from Aud5.Avstralija import problem
#
# if __name__ == '__main__':
#     solvers={
#         "BacktrackingSolver":BacktrackingSolver(),
#         "RecursiveBacktrackingSolver":RecursiveBacktrackingSolver(),
#         "MinConflictsSolver":MinConflictsSolver()
#     }
#     problem=Problem()
#     solver=input()
#     problem.setSolver(solvers.get(solver))
#     variables=[i for i in range(81)]
#     domain=list(range(1,10))
