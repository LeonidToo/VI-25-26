from constraint import Problem, BacktrackingSolver, AllDifferentConstraint


def read_input():
    num_families = int(input())
    families = {}
    for _ in range(num_families):
        name, size, reqs_string = input().split()
        reqs = reqs_string.split('-')
        families[name] = {'size': int(size), 'requirements': reqs}

    num_rooms = int(input())
    rooms = {}
    for _ in range(num_rooms):
        room_id, capacity, amenities_string = input().split()
        floor = room_id[0]
        amenities = amenities_string.split('-')
        rooms[int(room_id)] = {'floor': int(floor), 'capacity': int(capacity), 'amenities': amenities}

    return families, rooms



if __name__ == '__main__':
    problem = Problem(solver=BacktrackingSolver())

    families, rooms = read_input()
    # print(families,rooms)
    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.
    # print(rooms,families)
    variables=[key for key in families.keys()]
    domain=[key for key in rooms.keys()]
    no=len(variables)
    # for n in range(1,no+1):
    #     domain.append(f'No{n}')
    # problem.addVariables(variables, domain)
    i=1
    for var in variables:
        domtemp = []
        for dom in domain:
            dodadi=True
            if families[var]["size"]<=rooms[dom]["capacity"]:
                for a in families[var]["requirements"]:
                    if not a in rooms[dom]["amenities"]:
                        dodadi=False
                        break
            else:
                continue
            if dodadi:
                domtemp.append(dom)
        domtemp.append(f'No{i}')
        i+=1
        problem.addVariable(var,domtemp)
    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.

    problem.addConstraint(AllDifferentConstraint(),variables)

    def constraint_1(room,family_name):
        no="No"
        if no in str(room):
            # print("da")
            return True
        room_info=rooms[room]
        family_info=families[family_name]
        rf,rc,rs=room_info["floor"],room_info["capacity"],room_info["amenities"]
        fc,fs=family_info["size"],family_info["requirements"]
        if fc<=rc:
            for a in fs:
                if not a in rs:
                    return False
            return True
        return False
    for key in families.keys():
        problem.addConstraint(lambda family,famil_name=key:constraint_1(family,famil_name),[key])
    solutions = problem.getSolutions()  # Ne menuvaj! Do not modify!

    # Ispechatete go najdobroto reshenie vo baraniot format.
    # Print the best solution in the required format.
    best_sol=None
    best_total=-1
    for sol in solutions:
        total=0
        no="No"
        names_remove=[]
        for name in sol:
            if not no in str(sol[name]):
                total+=families[name]["size"]
            else:
                names_remove.append(name)
            if total>best_total:
                best_sol=sol
                best_total=total
        for name in names_remove:
            del sol[name]
    print("Best assignment:")
    if best_sol:
        for name, room in sorted(best_sol.items(), key=lambda x: x[1]):
            print(f"{name}->{room}")