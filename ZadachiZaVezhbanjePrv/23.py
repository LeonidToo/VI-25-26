from constraint import *

if __name__ == '__main__':

    bands = dict()

    band_info = input()
    while band_info != 'end':
        band, time, genre = band_info.split(' ')
        bands[band] = (time, genre)
        band_info = input()

    # Add the variables here
    rock_var=[]
    metal_var=[]
    punk_var=[]
    variables=[]
    for band,(genre,time) in bands.items():
        if genre=="rock":
            rock_var.append(band)
            variables.append(band)
        elif genre=="metal":
            variables.append(band)
            metal_var.append(band)
        else:
            variables.append(band)
            punk_var.append(band)


    domain = [f'S{i + 1}' for i in range(3)]

    problem = Problem(BacktrackingSolver())

    # Change this section if necessary
    problem.addVariables(variables, domain)

    # Add the constraints here


    for band in variables:
        for bandb in variables:
            if bandb==band:
                continue
            if int(bands[band][1])==120 and int(bands[bandb][1])==120:
                problem.addConstraint(AllDifferentConstraint(),[band,bandb])
    band_80=[]
    for band in variables:
        if int(bands[band][1])<80:
            band_80.append(band)
    def constraint_1(*all_vars):
        stages=[0,0,0,0]
        for var in all_vars:
            stages[int(var[1])]+=1
        for i in range(4):
            if stages[i]>5:
                return False
        return True
    problem.addConstraint(constraint_1,band_80)
    time = 0
    if len(rock_var)>0:
        for band in rock_var:
            time += int(bands[band][1])
        if time <= 300:
            problem.addConstraint(AllEqualConstraint(), rock_var)
    time = 0
    if len(metal_var)>0:
        for band in metal_var:
            time += int(bands[band][1])
        if time <= 300:
            problem.addConstraint(AllEqualConstraint(), metal_var)
    time = 0
    if len(punk_var)>0:
        for band in punk_var:
            time += int(bands[band][1])
        if time <= 300:
            problem.addConstraint(AllEqualConstraint(), punk_var)
    result = problem.getSolution()

    # Add the printing section here
    for var in variables:
        print(f'{var} ({bands[var]}): {result[var]}')
