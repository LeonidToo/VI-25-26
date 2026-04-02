from searching_framework import *

People= {(3, 3), (5, 4)}
net={(7,2),(7,3)}
Movement={"up":(0,1),"down":(0,-1),"right":(1,0),"up-right":(1,1),"down-right":(1,-1)}
Around={(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)}
class Fudbal(Problem):
    def __init__(self,people,net,initial,goal=None):
        super().__init__(initial,goal)
        self.people=people
        self.net=net
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        ball=(state[2],state[3])
        if ball in self.net:
            return True
        return False
    def check_valid(self,state):
        nx,ny,topka_nx,topka_ny=state
        nov_pos = (nx, ny)
        if not (0 <= nx < 8) or not (0 <= ny < 6) or nov_pos in self.people:
            return False
        if not (0 <= topka_nx < 8) or not (0 <= topka_ny < 6):
            return False
        for jx, jy in Around:
            if (topka_nx + jx, topka_ny + jy) in self.people:
                return False
        return True
    def successor(self, state):
        rez={}
        x,y,topka_x,topka_y=state
        topka=(topka_x,topka_y)
        chisto=True
        for action, (dx,dy) in Movement.items():
            nx,ny =x+dx, y+dy
            nov_pos=(nx,ny)
            if nov_pos!=topka:
                if self.check_valid((nx,ny,topka_x,topka_y)):
                    rez["Move man "+action]=(nx,ny,topka_x,topka_y)
            else:
                topka_nx,topka_ny=topka_x+dx,topka_y+dy
                if self.check_valid((nx,ny,topka_nx,topka_ny)):
                    rez["Push ball "+action]=(nx,ny,topka_nx,topka_ny)
        return rez


if __name__ == '__main__':
    pos=tuple(map(int, input().split(',')))
    pos_topka=tuple(map(int, input().split(',')))
    fudbal=Fudbal(People,net,(pos[0],pos[1],pos_topka[0],pos_topka[1]))
    rezultat=breadth_first_graph_search(fudbal)
    if rezultat:
        print(rezultat.solution())
    else:
        print("No Solution!")