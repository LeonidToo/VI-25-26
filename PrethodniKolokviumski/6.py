from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    movies = dict()

    n = int(input())
    for _ in range(n):
        film_info = input()
        film, genre, time = film_info.split(' ')
        movies[film] = (float(time), genre)

    l_days = int(input())

    # Tuka definirajte gi promenlivite i domenite
    # Tuka definirajte gi promenlivite i domenite
    domain = []
    for i in range(1, l_days + 1):
        for j in range(12, 24):
            domain.append(f'Day {i} {j}:00 - Cinema 1')
            domain.append(f'Day {i} {j}:00 - Cinema 2')

    domain_child = []
    for i in range(1, l_days + 1):
        for j in range(12, 19):
            domain_child.append(f'Day {i} {j}:00 - Cinema 1')
            domain_child.append(f'Day {i} {j}:00 - Cinema 2')

    sci_fi_var = []
    action_var = []
    horror_var = []

    # Add variables one by one exactly in the original order
    for film, (time, genre) in movies.items():
        if genre == "children's":
            problem.addVariable(film, domain_child)
        else:
            problem.addVariable(film, domain)

        # Keep track of specific genres for the same-cinema constraint
        if genre == "action":
            action_var.append(film)
        elif genre == "horror":
            horror_var.append(film)
        elif genre == "sci-fi":
            sci_fi_var.append(film)
    # Tuka dodadete gi ogranichuvanjata
    pairs=[]
    for film in movies:
        for filmb in movies:
            if (filmb,film) in pairs or filmb==film:
                continue
            pairs.append((film,filmb))
    def constraint_1(a,b,imea,imeb):
        day_a=int(a[4])
        cinema_a=int(a[-1])
        time_a=(int(a[6])*10)+int(a[7])
        day_b=int(b[4])
        cinema_b=int(b[-1])
        time_b=(int(b[6])*10)+int(b[7])
        if day_a==day_b and cinema_a==cinema_b:
            if time_a==time_b:
                return False
            if time_a<time_b:
                xd=time_a+movies[imea][0]
                return time_a+movies[imea][0]<time_b
            else:
                xd=time_b+movies[imeb][0]
                return time_b+movies[imeb][0]<time_a
        return True
        print(a)
        print(b)

    for pair in pairs:
        problem.addConstraint(lambda a,b,aname=pair[0],bname=pair[1]:constraint_1(a,b,aname,bname),[pair[0],pair[1]])

    def constraint_2(*all_vars):
        cinemaas=[]
        for film in all_vars:
            cinemaas.append(int(film[-1]))
        cinemaas=set(cinemaas)
        return len(cinemaas)==1
    if len(sci_fi_var)>0:
        problem.addConstraint(constraint_2,sci_fi_var)
    if len(action_var)>0:
        problem.addConstraint(constraint_2,action_var)
    if len(horror_var)>0:
        problem.addConstraint(constraint_2,horror_var)
    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    if result:
        for movie in movies:
            print(f'{movie}: {result[movie]}')
    else:
        print("No Solution!")