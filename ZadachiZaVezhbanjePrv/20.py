from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # Add the domains
    problem.addVariable("Marija_attendance", [0,1])
    problem.addVariable("Simona_attendance", [1])
    problem.addVariable("Petar_attendance", [0,1])
    problem.addVariable("time_meeting", list(range(12,21)))
    # ----------------------------------------------------
    simona_time=[13,14,16,19]
    marija_time=[14,15,18]
    petar_time=[12,13,16,17,18,19]
    # ---Add the constraints----------------
    def constraint_1(*all_vars):
        m,s,p,t=all_vars
        if not t in simona_time:
            return False
        if m==0 and p==0:
            return False
        if m==1 and not t in marija_time:
            return False
        if p==1 and not t in petar_time:
            return False
        return True
    problem.addConstraint(constraint_1,["Marija_attendance","Simona_attendance","Petar_attendance","time_meeting"])
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]
