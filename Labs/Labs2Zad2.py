from searching_framework import Problem, astar_search

dir = {"Up": (0, 1), "Down": (0, -1), "Left": (-1, 0), "Right": (1, 0)}

class Roobot(Problem):
    def __init__(self,walls,max_bat,stations,initial,goal=None):
        super().__init__(initial,goal)
        self.walls=walls
        self.max_battery=max_bat
        self.stations=stations
    def check_valid(self,state):
        x,y,b=state
        pos=(x,y)
        if 0<=x<10 and 0<=y<10:
            if pos in self.walls:
                return False
            else:
                return True
        else:
            return False
    def successor(self, state):
        rez={}
        x,y,batery=state
        if batery>0:
            for action, (dx, dy) in dir.items():
                nbatery = batery
                if (x, y) in self.stations:
                    nbatery = self.max_battery
                nx, ny = x + dx, y + dy
                if self.check_valid((nx, ny, nbatery-1)):
                    rez[action] = (nx, ny, nbatery-1)
        return rez
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        x,y,b=state
        return (x,y)==self.goal
    def h(self,node):
        state=node.state
        x,y,b=state
        count=0
        count=abs(self.goal[0]-x)+abs(self.goal[1]-y)
        if count>b:
            man_station=100 #ovoa ko mn golem broj
            for pos in self.stations:
                man_station=min(man_station,(abs(pos[0]-x)+abs(pos[1]-y)))
            count+=man_station
        return count
if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    # your code here
    WALLS = [
        (0, 9), (1, 9), (2, 9), (3, 9),(0, 7), (1, 7),(3, 6),(7, 6), (8, 6), (9, 6),(4, 0), (5, 0),
    ]
    robot=tuple(map(int,input().split(',')))
    goal=tuple(map(int,input().split(',')))
    batery=int(input())
    stations=int(input())
    stations_loc=tuple([tuple(map(int, input().split(','))) for _ in range(stations)])
    problem=Roobot(WALLS,batery,stations_loc,(robot[0],robot[1],batery),(goal[0],goal[1]))
    rez=astar_search(problem)
    if rez:
        print(rez.solution())
    else:
        print("No Solution!")
