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
    Dijag=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
    pairs=[]
    problem.addConstraint(AllDifferentConstraint(),variables)
    for var in variables:
        for varr in variables:
            if (varr,var) in pairs or var==varr:
                continue
            pairs.append([var,varr])
    def constraint_1(a,b):
        (x1,y1),(x2,y2)=a,b
        for (dx,dy) in Dijag:
            if (x1+dx,y1+dy)==(x2,y2):
                return False
        return True
    for a,b in pairs:
        problem.addConstraint(constraint_1,[a,b])


    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----
    # print(solution)
    for var in variables:
        print(f'{solution[var][0]} {solution[var][1]}')

