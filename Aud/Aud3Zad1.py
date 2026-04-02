from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Adventure(Problem):
    def __init__(self,initial,goal=None):
        super().__init__(initial,goal)
    def successor(self, state):
        rez=dict()
        r,c,pr1,pc1,prd1,pr2,pc2,prd2=state
        if (r,c)==(pr1,pc1) or (r,c)==(pr2,pc2):
            return rez
        if prd1==1:
            pr1+=1
            if pr1==5:
                prd1=0
        else:
            pr1 -= 1
            if pr1 == 0:
                prd1 = 1
        if prd2==1:
            pr2+=1
            if pr2==5:
                prd2=0
        else:
            pr2 -= 1
            if pr2 == 0:
                prd2 = 1
        if r-1>=0:
            rez["Up"]=(r-1,c,pr1,pc1,prd1,pr2,pc2,prd2)
        if r+1<6:
            rez["Down"]=(r+1,c,pr1,pc1,prd1,pr2,pc2,prd2)
        if c+1<9:
            rez["Right"]=(r,c+1,pr1,pc1,prd1,pr2,pc2,prd2)
        if c-1>=0:
            rez["Left"]=(r,c-1,pr1,pc1,prd1,pr2,pc2,prd2)
        return rez
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        r1,c1,a,b,c,d,e,f=state
        rez=(r1,c1)
        return self.goal==rez

if __name__=='__main__':
    avantura=Adventure((3,0,0,2,1,5,5,0),(1,7))
    rez=breadth_first_graph_search(avantura)
    rez1=depth_first_graph_search(avantura)
    print(rez.solution())
    print(rez.solve())