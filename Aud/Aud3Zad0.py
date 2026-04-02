from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Container(Problem):
    def __init__(self,capacity,initial,goal=None):
        super().__init__(initial,goal)
        self.capacity=capacity
    def successor(self, state):
        j1,j2=state
        c1,c2=self.capacity
        results=dict()
        if j1>0:
            results["J1 praznenje"]=(0,j2)
        if j2>0:
            results["J2 praznenje"]=(j1,0)
        if j1>0 and j2<c2:
            razlika=min(c2-j2,j1)
            results["J1 se pretura vo J2"]=(j1-razlika,j2+razlika)
        if j2>0 and j1<c1:
            razlika=min(c1-j1,j2)
            results["J2 se pretura vo J1"]=(j1+razlika,j2-razlika)
        return results
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state==self.goal

if __name__=='__main__':
    kontenjer=Container([130,150],(100,30),(120,10))
    rez=breadth_first_graph_search(kontenjer)
    print(rez.state)
    print(rez.action)