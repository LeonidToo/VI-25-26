from searching_framework import *
# from utils import *
# from uninformed_search import *
# from informed_search import *

Direction=[(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]
Movement={"Gore":(0,1),"Desno":(1,0)}

class Boxes(Problem):
    def __init__(self,boxes,n, initial, goal=None):
        super().__init__(initial, goal)
        self.n=n
        self.boxes=boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        pos,boxes=state
        return len(boxes)==0
    def check_valid(self,state):
        (x,y),boxes=state
        return 0<=x<self.n and 0<=y<self.n and not (x,y) in self.boxes
    def successor(self, state):
        rez={}
        (x,y),boxes=state
        for action,(dx,dy) in Movement.items():
            nx,ny=x+dx,y+dy
            n_boxes=list(boxes)
            for (bx,by) in Direction:
                if (nx+bx,ny+by) in n_boxes:
                    n_boxes.remove((nx+bx,ny+by))
            if self.check_valid(((nx,ny),tuple(n_boxes))):
                rez[action]=((nx,ny),tuple(n_boxes))
        return rez


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
    boxes=tuple(boxes)
    problem=Boxes(boxes,n,(man_pos,boxes))
    rezultat=breadth_first_graph_search(problem)
    if rezultat:
        print(rezultat.solution())
    else:
        print("No Solution!")