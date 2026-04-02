from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Define the variables
    variables=[]

    for name,topic in papers.items():
        variables.append(f'{name} ({topic})')

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    var_AI=[]
    var_ML=[]
    var_NLP=[]
    for name, topic in papers.items():
        var_AI.append(f'{name} ({topic})') if topic=="AI" else ''
        var_ML.append(f'{name} ({topic})') if topic=="ML" else ''
        var_NLP.append(f'{name} ({topic})') if topic=="NLP" else ''


    # Change this section if necessary
    problem.addVariables(variables, domain)

    # Add the constraints
    def constraint_1(*vars):
        for a in domain:
            if vars.count(a)>4:
                return False
        return True
    problem.addConstraint(constraint_1,variables)
    if 0<len(var_AI)<=4:
        problem.addConstraint(AllEqualConstraint(),var_AI)
    if 0<len(var_ML)<=4:
        problem.addConstraint(AllEqualConstraint(),var_ML)
    if 0<len(var_NLP)<=4:
        problem.addConstraint(AllEqualConstraint(),var_NLP)


    result = problem.getSolution()

    # Add the required print section
    for name,topic in papers.items():
        var=f'{name} ({topic})'
        print(f'{var}: {result[var]}')
