from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lecture_slots_AI = int(input())
    lecture_slots_ML = int(input())
    lecture_slots_R = int(input())
    lecture_slots_BI = int(input())

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                         "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_exercises_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Add the variables here--------------------
    variables=[]
    var_ai_l=[]
    var_ml_l=[]
    var_r_l=[]
    var_bi_l=[]
    for i in range(1,lecture_slots_AI+1):
        var_ai_l.append(f'AI_lecture_{i}')
        variables.append(f'AI_lecture_{i}')
    for i in range(1,lecture_slots_ML+1):
        var_ml_l.append(f'ML_lecture_{i}')
        variables.append(f'ML_lecture_{i}')

    for i in range(1,lecture_slots_R+1):
        var_r_l.append(f'R_lecture_{i}')
        variables.append(f'R_lecture_{i}')

    for i in range(1,lecture_slots_BI+1):
        var_bi_l.append(f'BI_lecture_{i}')
        variables.append(f'BI_lecture_{i}')


    problem.addVariables(var_ai_l,AI_lectures_domain)
    problem.addVariables(var_ml_l,ML_lectures_domain)
    problem.addVariables(var_r_l,R_lectures_domain)
    problem.addVariables(var_bi_l,BI_lectures_domain)
    problem.addVariables(["AI_exercises"],AI_exercises_domain),variables.append("AI_exercises")
    problem.addVariables(["ML_exercises"],ML_exercises_domain),variables.append("ML_exercises")
    problem.addVariables(["BI_exercises"],BI_lectures_domain),variables.append("BI_exercises")
    # ---Add the constraints here----------------
    problem.addConstraint(AllDifferentConstraint(),variables)
    pairs=[]
    for var in variables:
        for varr in variables:
            if (varr,var) in pairs or varr==var:
                continue
            pairs.append((var,varr))
    def constraint_1(a,b):
        if a[0]==b[0] and a[1]==b[1] and a[2]==b[2]:
            a_vreme=int(a[-2])*10+int(a[-1])
            b_vreme=int(b[-2])*10+int(b[-1])
            return abs(a_vreme-b_vreme)>2
        return True
    for (a,b) in pairs:
        problem.addConstraint(lambda a,b:constraint_1(a,b),[a,b])
    def constraint_2(a,b):
        a_vreme = int(a[-2]) * 10 + int(a[-1])
        b_vreme = int(b[-2]) * 10 + int(b[-1])
        return a_vreme==b_vreme
    pairs_ml=[]
    var_ml_l.append("ML_exercises")
    for var in var_ml_l:
        for varr in var_ml_l:
            if (varr, var) in pairs or varr == var:
                continue
            pairs.append((var, varr))
    for (a,b) in pairs_ml:
        problem.addConstraint(lambda a,b:constraint_2(a,b),[a,b])
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)