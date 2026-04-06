from searching_framework import *

dirs={"Gore":(0,+1),"Dolu":(0,-1),"Levo":(-1,0),"Desno":(+1,0),"Stoj":(0,0)}
class Laser(Problem):
    def __init__(self,row,col,walls, initial, goal):
        super().__init__(initial, goal)
        self.n = row
        self.m = col
        self.walls=walls


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_pos,laser_pos,timer=state
        return man_pos==self.goal

    def check_valid(self,state):
        (x_man, y_man), (x_laser, y_laser), timer = state
        if timer==4 and (x_man==x_laser or y_man==y_laser):
            return False
        return not ((x_man,y_man) in self.walls) and 0<=x_man<self.m and 0<=y_man<self.n

    def successor(self, state):
        rez={}
        (x_man,y_man),(x_laser,y_laser),timer=state
        if timer==1:
            (x_laser,y_laser)=(x_man,y_man)
        for action,(dx,dy) in dirs.items():
            nx,ny=x_man+dx,y_man+dy
            ntimer=timer+1 if timer+1<5 else 1
            if self.check_valid(((nx,ny),(x_laser,y_laser),ntimer)):
                rez[action]=((nx, ny), (x_laser, y_laser), ntimer)
        return rez


read_two = lambda: tuple(map(int, input().split()))
if __name__ == '__main__':
    N, M = read_two()
    man_pos = read_two()
    target_pos = read_two()
    timer = int(input())
    laser_pos = read_two()
    blocked = [read_two() for _ in range(int(input()))]

    problem = Laser(N,M,blocked,(man_pos,laser_pos,timer),target_pos)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")