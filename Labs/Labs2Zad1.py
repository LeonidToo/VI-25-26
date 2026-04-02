from math import ceil

from searching_framework import Problem, astar_search
Actions={"Gore":(0,1),"Dolu":(0,-1),"Levo":(-1,0),"Desno 2":(2,0),"Desno 3":(3,0)}
class Labyrinth(Problem):
    def __init__(self,walls,n,initial,goal=None):
        super().__init__(initial,goal)
        self.walls=walls
        self.n=n
    def checkValid(self,state,desno):
        x,y=state
        if not desno:
            if 0 <= x < self.n and 0 <= y < self.n and not ((x, y) in self.walls):
                return True
            else:
                return False
        else:
            if 0 <= x < self.n and 0 <= y < self.n and not((x, y) in self.walls or (x-1, y) in self.walls or (x-2, y) in self.walls):
                return True
            else:
                return False
    def successor(self, state):
        rez={}
        x,y=state
        for action,(dx,dy) in Actions.items():
            desno=False
            if dx>0:
                desno=True
            nx,ny=x+dx,y+dy
            if desno:
                if self.checkValid((nx, ny),True):
                    rez[action] = (nx, ny)
            else:
                if self.checkValid((nx, ny),False):
                    rez[action] = (nx, ny)
        return rez
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        x,y=state
        pos=(x,y)
        return pos==self.goal
    def h(self,node):
        state=node.state
        x,y=state
        vert=abs(y-self.goal[1])
        hor=x-self.goal[0]
        if hor<0:
            return abs(hor)+vert
        else:
            return ceil(hor/3)+vert
        # return abs(x-self.goal[0])+abs(y-self.goal[1])
if __name__ == '__main__':
    # your code here
    n=int(input())
    m=int(input())
    walls=tuple([tuple(map(int, input().split(','))) for _ in range(m)])
    person=tuple(map(int,input().split(',')))
    house=tuple(map(int,input().split(',')))
    lavirint=Labyrinth(walls,n,(person[0],person[1]),(house[0],house[1]))
    rez=astar_search(lavirint)
    if rez:
        print(rez.solution())
    else:
        print("No Solution!")