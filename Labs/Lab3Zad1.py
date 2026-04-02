from constraint import Problem, BacktrackingSolver, AllDifferentConstraint

def neigbours(star1, star2):
    (x, y), (x1, y1)=star1,star2
    if x+1==x1 or x-1==x1:
        return True
    if y+1==y1 or y-1==y1:
        return True
    return False

if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]
    N = max(map(max, grid))  # Number of regions

    problem = Problem(solver=BacktrackingSolver())

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.
    variables=[f'S{i}' for i in range(N)]
    # for i in range(1,N+1):
    #     variables.append(f'S{i}')
    domain=[(i,j) for i in range(K) for j in range(K)]
    problem.addVariables(variables,domain)

    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.

    # Constraint 1: maks dve u eden region
    problem.addConstraint(AllDifferentConstraint(), variables)

    def constraint_1(*ass_variables):
        count=[0 for _ in range(N+1)]
        for r,c in ass_variables:
            count[grid[r][c]]+=1
            if count[grid[r][c]]>2:
                return False
        return True
    problem.addConstraint(constraint_1,variables)

    # Constraint 2:If different regions no same row and column, else no neighbours
    star_comb=[]
    for star in variables:
        for star1 in variables:
            if not [star1,star] in star_comb and star !=star1:
                star_comb.append([star,star1])
    def constraint_2(star1,star2):
        if grid[star1[0]][star1[1]]==grid[star2[0]][star2[1]]:
            if neigbours(star1,star2):
                return False
            return True
        else:
            if star1[0]==star2[0] or star1[1]==star2[1]:
                return False
            return True
    for combo in star_comb:
        problem.addConstraint(constraint_2,combo)
    result = problem.getSolution()

    # Ispechatete go reshenieto vo baraniot format.
    # Print the solution in the required format.

    if result:
        for star,(x,y) in result.items():
            grid[x][y]='*'
        for i in range(K):
            row=""
            for j in range(K):
                row+=str(grid[i][j])+" "
            print(row)

    else:
        print("No Solution!")
