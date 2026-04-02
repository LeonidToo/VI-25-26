from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Stars(Problem):
    def __init__(self,star_pos,initial,goal=None):
        super().__init__(initial,goal)
        self.star_pos=star_pos
    def successor(self, state):
        rez=dict()
        s1x,s1y=self.star_pos[0]
        s2x,s2y=self.star_pos[1]
        s3x,s3y=self.star_pos[2]
        kx,ky,bx,by,s1,s2,s3=state
        if 0<= kx-1 <8 and 0 <= ky+2 <8:
            if s1x==kx-1 and s1y==ky+2:
                rez["K1"] = (kx - 1, ky + 2, bx, by, True, s2, s3)
            elif s2x == kx-1 and s2y == ky+2:
                rez["K1"] = (kx - 1, ky + 2, bx, by, s1, True, s3)
            elif s3x == kx-1 and s3y == ky+2:
                rez["K1"] = (kx - 1, ky + 2, bx, by, s1, s2, True)
            else:
                rez["K1"]=(kx-1,ky+2,bx,by,s1,s2,s3)
        if 0<= kx + 1 < 8 and 0<= ky + 2 < 8:
            if s1x == kx+ 1 and s1y == ky+2:
                rez["K2"] = (kx + 1, ky + 2, bx, by, True, s2, s3)
            elif s2x == kx+ 1 and s2y == ky+2:
                rez["K2"] = (kx + 1, ky + 2, bx, by, s1, True, s3)
            elif s3x == kx+ 1 and s3y == ky+2:
                rez["K2"] = (kx + 1, ky + 2, bx, by, s1, s2, True)
            else:
                rez["K2"] = (kx + 1, ky + 2, bx, by, s1, s2, s3)
        if 0<= kx + 2 < 8 and 0<= ky + 1 < 8:
            if s1x == kx+ 2 and s1y == ky+ 1:
                rez["K3"] = (kx + 2, ky + 1, bx, by, True, s2, s3)
            elif s2x == kx+ 2 and s2y == ky+ 1:
                rez["K3"] = (kx + 2, ky + 1, bx, by, s1, True, s3)
            elif s3x == kx+ 2 and s3y == ky+ 1:
                rez["K3"] = (kx + 2, ky + 1, bx, by, s1, s2, True)
            else:
                rez["K3"] = (kx + 2, ky + 1, bx, by, s1, s2, s3)
        if 0<= kx + 2 < 8 and 0<= ky - 1 < 8:
            if s1x == kx+ 2 and s1y == ky- 1:
                rez["K4"] = (kx + 2, ky - 1, bx, by, True, s2, s3)
            elif s2x == kx+ 2 and s2y == ky- 1:
                rez["K4"] = (kx + 2, ky - 1, bx, by, s1, True, s3)
            elif s3x == kx+ 2 and s3y == ky- 1:
                rez["K4"] = (kx + 2, ky - 1, bx, by, s1, s2, True)
            else:
                rez["K4"] = (kx + 2, ky - 1, bx, by, s1, s2, s3)
        if 0 <= kx + 1 < 8 and 0 <= ky - 2 < 8:
            if s1x == kx+ 1 and s1y == ky- 2:
                rez["K5"] = (kx + 1, ky - 2, bx, by, True, s2, s3)
            elif s2x == kx+ 1 and s2y == ky- 2:
                rez["K5"] = (kx + 1, ky - 2, bx, by, s1, True, s3)
            elif s3x == kx+ 1 and s3y == ky- 2:
                rez["K5"] = (kx + 1, ky - 2, bx, by, s1, s2, True)
            else:
                rez["K5"] = (kx + 1, ky - 2, bx, by, s1, s2, s3)
        if 0 <= kx - 1 < 8 and 0 <= ky - 2 < 8:
            if s1x == kx- 1 and s1y == ky- 2:
                rez["K6"] = (kx - 1, ky - 2, bx, by, True, s2, s3)
            elif s2x == kx- 1 and s2y == ky- 2:
                rez["K6"] = (kx - 1, ky - 2, bx, by, s1, True, s3)
            elif s3x == kx- 1 and s3y == ky- 2:
                rez["K6"] = (kx - 1, ky - 2, bx, by, s1, s2, True)
            else:
                rez["K6"] = (kx - 1, ky - 2, bx, by, s1, s2, s3)
        if 0 <= kx - 2 < 8 and 0 <= ky - 1 < 8:
            if s1x == kx- 2 and s1y == ky- 1:
                rez["K7"] = (kx - 2, ky - 1, bx, by, True, s2, s3)
            elif s2x == kx- 2 and s2y == ky- 1:
                rez["K7"] = (kx - 2, ky - 1, bx, by, s1, True, s3)
            elif s3x == kx- 2 and s3y == ky- 1:
                rez["K7"] = (kx - 2, ky - 1, bx, by, s1, s2, True)
            else:
                rez["K7"] = (kx - 2, ky - 1, bx, by, s1, s2, s3)
        if 0 <= kx - 2 < 8 and 0 <= ky + 1 < 8:
            if s1x == kx- 2 and s1y == ky+ 1:
                rez["K8"] = (kx - 2, ky + 1, bx, by, True, s2, s3)
            elif s2x == kx- 2 and s2y == ky+ 1:
                rez["K8"] = (kx - 2, ky + 1, bx, by, s1, True, s3)
            elif s3x == kx- 2 and s3y == ky+ 1:
                rez["K8"] = (kx - 2, ky + 1, bx, by, s1, s2, True)
            else:
                rez["K8"] = (kx - 2, ky + 1, bx, by, s1, s2, s3)
        if 0 <= bx - 1 < 8 and 0 <= by + 1 < 8:
            if s1x == bx- 1 and s1y == by+ 1:
                rez["B1"]=(kx,ky,bx-1,by+1,True,s2,s3)
            elif s2x == bx- 1 and s2y == by+ 1:
                rez["B1"] = (kx, ky, bx - 1, by + 1, s1, True, s3)
            elif s3x == bx- 1 and s3y == by+ 1:
                rez["B1"] = (kx, ky, bx - 1, by + 1, s1, s2, True)
            else:
                rez["B1"]=(kx,ky,bx-1,by+1,s1,s2,s3)
        if 0 <= bx + 1 < 8 and 0 <= by + 1 < 8:
            if s1x == bx + 1 and s1y == by + 1:
                rez["B2"] = (kx, ky, bx + 1, by + 1, True, s2, s3)
            elif s2x == bx + 1 and s2y == by + 1:
                rez["B2"] = (kx, ky, bx + 1, by + 1, s1, True, s3)
            elif s3x == bx + 1 and s3y == by + 1:
                rez["B2"] = (kx, ky, bx + 1, by + 1, s1, s2, True)
            else:
                rez["B2"] = (kx, ky, bx + 1, by + 1, s1, s2, s3)
        if 0 <= bx - 1 < 8 and 0 <= by - 1 < 8:
            if s1x == bx - 1 and s1y == by - 1:
                rez["B3"] = (kx, ky, bx - 1, by - 1, True, s2, s3)
            elif s2x == bx - 1 and s2y == by - 1:
                rez["B3"] = (kx, ky, bx - 1, by - 1, s1, True, s3)
            elif s3x == bx - 1 and s3y == by - 1:
                rez["B3"] = (kx, ky, bx - 1, by - 1, s1, s2, True)
            else:
                rez["B3"] = (kx, ky, bx - 1, by - 1, s1, s2, s3)
        if 0 <= bx + 1 < 8 and 0 <= by - 1 < 8:
            if s1x == bx + 1 and s1y == by - 1:
                rez["B1"] = (kx, ky, bx + 1, by - 1, True, s2, s3)
            elif s2x == bx + 1 and s2y == by - 1:
                rez["B1"] = (kx, ky, bx + 1, by - 1, s1, True, s3)
            elif s3x == bx + 1 and s3y == by - 1:
                rez["B1"] = (kx, ky, bx + 1, by - 1, s1, s2, True)
            else:
                rez["B1"] = (kx, ky, bx + 1, by - 1, s1, s2, s3)
        return rez
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        if state[4] and state[5] and state[6]:
            return True
        return False



if __name__=='__main__':
    knight = [2, 5]
    bishop = [5, 1]
    stars_pos = ((1, 1), (4, 3), (6, 6))
    Dzvezda=Stars(stars_pos,(knight[0],knight[1],bishop[0],bishop[1],False,False,False))
    rezultat=breadth_first_graph_search(Dzvezda)
    print(rezultat.solution())