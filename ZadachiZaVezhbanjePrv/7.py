# from searching_framework import *
#
#
# class Robot(Problem):
#     def __init__(self,walls, initial, goal=None):
#         super().__init__(initial, goal)
#         self.walls=walls
#
#     def actions(self, state):
#         return self.successor(state).keys()
#
#     def result(self, state, action):
#         return self.successor(state)[action]
#
#     def goal_test(self, state):
#         if state[2]==0 and state[4]==0:
#             return True
#         return False
#
#     def successor(self, state):
#         rez=dict()
#         walls=self.walls
#         x,y=state[0]
#         m1_x,m1_y=state[1]
#         m1_s=state[2]
#         m2_x,m2_y=state[3]
#         m2_s=state[4]
#         m1=state[5]
#         m1_xy=state[6]
#         m2=state[7]
#         m2_xy=state[8]
#         if x==m1_x and y==m1_y and m1==0 and m1_s!=0:
#             rez["Repair"]=((x,y),(m1_x,m1_y),m1_s-1,(m2_x,m2_y),m2_s,m1,m1_xy,m2,m2_xy)
#             if not ((x, y + 1) in walls) and y + 1 < 10:
#                 rez["Up"] = ((x, y + 1), (m1_x, m1_y), m1_s + 2, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#             if not ((x, y - 1) in walls) and y - 1 >= 0:
#                 rez["Down"] = ((x, y - 1), (m1_x, m1_y), m1_s + 2, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#             if not ((x - 1, y) in walls) and x - 1 >= 0:
#                 rez["Left"] = ((x - 1, y), (m1_x, m1_y), m1_s + 2, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#             if not ((x + 1, y) in walls) and x + 1 < 10:
#                 rez["Right"] = ((x + 1, y), (m1_x, m1_y), m1_s + 2, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#         else:
#             if x == m2_x and y == m2_y and m2 == 0 and m1_s == 0:
#                 rez["Repair"] = ((x, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s - 1, m1, m1_xy, m2, m2_xy)
#                 if not ((x, y + 1) in walls) and y + 1 < 10:
#                     rez["Up"] = ((x, y + 1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s + 2, m1, m1_xy, m2, m2_xy)
#                 if not ((x, y - 1) in walls) and y - 1 >= 0:
#                     rez["Down"] = ((x, y - 1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s + 2, m1, m1_xy, m2, m2_xy)
#                 if not ((x - 1, y) in walls) and x - 1 >= 0:
#                     rez["Left"] = ((x - 1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s + 2, m1, m1_xy, m2, m2_xy)
#                 if not ((x + 1, y) in walls) and x + 1 < 10:
#                     rez["Right"] = ((x + 1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s + 2, m1, m1_xy, m2, m2_xy)
#             if m1!=0 or m1_s!=0:
#                 if not((x,y+1) in walls) and y+1<10:
#                     if (x,y+1) in m1_xy:
#                         rez["Up"]=((x, y+1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1-1, tuple([s for s in m1_xy if s[0] != x or s[1] != y+1]), m2, m2_xy)
#                     else:
#                         rez["Up"]=((x, y+1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#                 if not ((x, y - 1) in walls) and y - 1 >= 0:
#                     if (x,y-1) in m1_xy:
#                         rez["Down"]=((x, y-1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1-1, tuple([s for s in m1_xy if s[0] != x or s[1] != y-1]), m2, m2_xy)
#                     else:
#                         rez["Down"]=((x, y-1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#                 if not ((x-1, y) in walls) and x - 1 >= 0:
#                     if (x-1,y) in m1_xy:
#                         rez["Left"]=((x-1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1-1, tuple([s for s in m1_xy if s[0] != x-1 or s[1] != y]), m2, m2_xy)
#                     else:
#                         rez["Left"]=((x-1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#                 if not ((x+1, y) in walls) and x + 1 <10:
#                     if (x+1,y) in m1_xy:
#                         rez["Right"]=((x+1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1-1, tuple([s for s in m1_xy if s[0] != x+1 or s[1] != y]), m2, m2_xy)
#                     else:
#                         rez["Right"]=((x+1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#             else:
#                 if not((x,y+1) in walls) and y+1<10:
#                     if (x,y+1) in m2_xy:
#                         rez["Up"]=((x, y+1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2-1, tuple([s for s in m2_xy if s[0] != x or s[1] != y+1]))
#                     else:
#                         rez["Up"]=((x, y+1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#                 if not ((x, y - 1) in walls) and y - 1 >= 0:
#                     if (x,y-1) in m2_xy:
#                         rez["Down"]=((x, y-1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2-1, tuple([s for s in m2_xy if s[0] != x or s[1] != y-1]))
#                     else:
#                         rez["Down"]=((x, y-1), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#                 if not ((x-1, y) in walls) and x - 1 >= 0:
#                     if (x-1,y) in m2_xy:
#                         rez["Left"]=((x-1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2-1, tuple([s for s in m2_xy if s[0] != x-1 or s[1] != y]))
#                     else:
#                         rez["Left"]=((x-1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#                 if not ((x+1, y) in walls) and x + 1 <10:
#                     if (x+1,y) in m2_xy:
#                         rez["Right"]=((x+1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2-1, tuple([s for s in m2_xy if s[0] != x+1 or s[1] != y]))
#                     else:
#                         rez["Right"]=((x+1, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)
#
#
#         return rez
#
# if __name__ == '__main__':
#     robot_start_pos = tuple(map(int, input().split(',')))
#     M1_pos = tuple(map(int, input().split(',')))
#     M1_steps = int(input())
#     M2_pos = tuple(map(int, input().split(',')))
#     M2_steps = int(input())
#     parts_M1 = int(input())
#     to_collect_M1 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M1)])
#     parts_M2 = int(input())
#     to_collect_M2 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M2)])
#
#     walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5), (1, 6), (1, 7), (0, 6), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9)]
#
#     problem = Robot(walls,(robot_start_pos,M1_pos,M1_steps,M2_pos,M2_steps,parts_M1,to_collect_M1,parts_M2,to_collect_M2))
#
#     result = breadth_first_graph_search(problem)
#     if result:
#         print(result.solution())
#     else:
#         print("No Solution!")
#
#         # ((x, y), (m1_x, m1_y), m1_s, (m2_x, m2_y), m2_s, m1, m1_xy, m2, m2_xy)

from searching_framework import *

Direction={"Up":(0,1),"Down":(0,-1),"Left":(-1,0),"Right":(1,0)}

class Robot(Problem):
    def __init__(self,walls, initial, goal=None):
        super().__init__(initial, goal)
        self.walls=walls

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if state[2]==0 and state[4]==0:
            return True
        return False

    def successor(self, state):
        rez={}
        pos,m1_pos,m1_s,m2_pos,m2_s,m1_p,m1_xy,m2_p,m2_xy=state
        x,y=pos
        m1_popraveno= m1_s==0
        m1_delovi=m1_p==0
        m2_popraveno= m2_s==0
        m2_delovi=m2_p==0
        walls=self.walls

        if m1_delovi and pos == m1_pos and not m1_popraveno:
            rez["Repair"]=(pos,m1_pos,m1_s-1,m2_pos,m2_s,m1_p,m1_xy,m2_p,m2_xy)
        if m1_popraveno and pos == m2_pos and m2_delovi:
            rez["Repair"] = (pos, m1_pos, m1_s, m2_pos, m2_s - 1, m1_p, m1_xy, m2_p, m2_xy)
        for action, (dx,dy) in Direction.items():
            nx,ny=x+dx,y+dy
            nov_pos=(nx,ny)
            n_m1_p, n_m1_xy=m1_p,m1_xy
            n_m2_p, n_m2_xy=m2_p,m2_xy
            n_m1_s=m1_s
            n_m2_s=m2_s
            if nov_pos in walls:
                continue
            if not(0<=nx<10) or not(0<=ny<10):
                continue
            if not m1_popraveno and nov_pos in m1_xy:
                n_m1_p-=1
                n_m1_xy=tuple([s for s in m1_xy if s!=nov_pos])
            elif m1_popraveno and nov_pos in m2_xy:
                n_m2_p-=1
                n_m2_xy=tuple([s for s in m2_xy if s!=nov_pos])
            if "Repair" in rez:
                n_m1_s+=2
            rez[action]=(nov_pos,m1_pos,n_m1_s,m2_pos,n_m2_s,n_m1_p,n_m1_xy,n_m2_p,n_m2_xy)
        return rez


if __name__ == '__main__':
    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())
    parts_M1 = int(input())
    to_collect_M1 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M1)])
    parts_M2 = int(input())
    to_collect_M2 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M2)])

    walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5), (1, 6), (1, 7), (0, 6), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9)]

    problem = Robot(walls,(robot_start_pos,M1_pos,M1_steps,M2_pos,M2_steps,parts_M1,to_collect_M1,parts_M2,to_collect_M2))

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")