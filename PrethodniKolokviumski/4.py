from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    m=int(input())
    # variables=[tuple(map(int,input().split(" "))) for _ in range(m)]
    variables=[]
    Tent_Pos=[(0,1),(0,-1),(1,0),(-1,0)]
    for _ in range(m):
        pos=tuple(map(int,input().split(" ")))
        variables.append(pos)
    pozicii=tuple(map(int,input().split(" ")))
    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    # problem.addVariable(..., ...)
    # problem.addVariables(..., ...)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------
    for var in variables:
        pos=var
        domain = [(pos[0] + dx, pos[1] + dy) for (dx, dy) in Tent_Pos if
                  (0 <= pos[0] + dx < 6 and 0 <= pos[1] + dy < 6 and not ((pos[0] + dx, pos[1] + dy) in variables))]
        problem.addVariable(pos, domain)
    problem.addConstraint(AllDifferentConstraint(),variables)
    def constraint_1(*all_vars):
        lista=list(pozicii)
        for (x,y) in all_vars:
            lista[x]-=1
        return lista==[0,0,0,0,0,0]

    problem.addConstraint(constraint_1,variables)
    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----
    # print(solution)
    for var in variables:
        print(f'{solution[var][0]} {solution[var][1]}')

