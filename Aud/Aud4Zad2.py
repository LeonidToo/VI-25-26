from searching_framework import *

class Molecule(Problem):
    def __init__(self,obstacles,initial,goal=None):
        super().__init__(initial,goal)
        self.matrix=[[0 for i in range(9)]for a in range(7)]
        for a in obstacles:
            self.matrix[6-a[1]][a[0]]='#'
        self.gridSize=[7,9]
    def successor(self, state):
        rez=dict()
        h1r,h1c,orr,oc,h2r,h2c=state
        h1=[h1r,h1c]
        o=[orr,oc]
        h2=[h2r,h2c]
        gridSizeR,gridSizeC=self.gridSize
        def RightX(moving,other1,other2):
            mr,mc=moving
            o1r, o1c=other1
            o2r, o2c=other2
            if mc+1>=gridSizeC:
                return [mr,mc]
            if self.matrix[mr][mc + 1]== '#' or (mc + 1 == o1c and mr == o1r) or (mc + 1 == o2c and mr == o2r):
                return [mr,mc]
            moving1=[mr,mc+1]
            return RightX(moving1,other1,other2)
        def LeftX(moving,other1,other2):
            mr, mc = moving
            o1r, o1c = other1
            o2r, o2c = other2
            if mc-1<0:
                return [mr,mc]
            if self.matrix[mr][mc - 1]== '#' or (mc - 1 == o1c and mr == o1r) or (mc - 1 == o2c and mr == o2r):
                return [mr,mc]
            moving1=[mr,mc-1]
            return LeftX(moving1,other1,other2)
        def UpX(moving,other1,other2):
            mr, mc = moving
            o1r, o1c = other1
            o2r, o2c = other2
            if mr-1<0:
                return [mr,mc]
            if self.matrix[mr-1][mc]== '#' or (mc == o1c and mr - 1 == o1r) or (mc == o2c and mr - 1 == o2r):
                return [mr,mc]
            moving1=[mr-1,mc]
            return UpX(moving1,other1,other2)
        def DownX(moving,other1,other2):
            mr, mc = moving
            o1r, o1c = other1
            o2r, o2c = other2
            if mr+1>=gridSizeR:
                return [mr,mc]
            if self.matrix[mr+1][mc]== '#' or (mc == o1c and mr + 1 == o1r) or (mc == o2c and mr + 1 == o2r):
                return [mr,mc]
            moving1=[mr+1,mc]
            return DownX(moving1,other1,other2)
        if RightX(h1, o, h2)!=h1:

            rez[f"RightH1"] = (RightX(h1, o, h2)[0],RightX(h1,o,h2)[1], o[0],o[1], h2[0],h2[1])
        if LeftX(h1, o, h2) != h1:
            rez[f"LeftH1"] = (LeftX(h1, o, h2)[0],LeftX(h1, o, h2)[1], o[0],o[1], h2[0],h2[1])
        if UpX(h1, o, h2) != h1:
            rez[f"UpH1"] = (UpX(h1, o, h2)[0],UpX(h1, o, h2)[1], o[0],o[1], h2[0],h2[1])
        if DownX(h1, o, h2) != h1:
            rez[f"DownH1"] = (DownX(h1, o, h2)[0],DownX(h1, o, h2)[1], o[0],o[1], h2[0],h2[1])
        if RightX(o, h1, h2) != o:
            rez[f"RightO"] = (h1[0],h1[1], RightX(o, h1, h2)[0],RightX(o, h1, h2)[1], h2[0],h2[1])
        if LeftX(o, h1, h2) != o:
            rez[f"LeftO"] = (h1[0],h1[1], LeftX(o, h1, h2)[0],LeftX(o, h1, h2)[1], h2[0],h2[1])
        if UpX(o, h1, h2) != o:
            rez[f"UpO"] = (h1[0],h1[1], UpX(o, h1, h2)[0],UpX(o, h1, h2)[1], h2[0],h2[1])
        if DownX(o, h1, h2) != o:
            rez[f"DownO"] = (h1[0],h1[1], DownX(o, h1, h2)[0],UpX(o, h1, h2)[1], h2[0],h2[1])
        if RightX(h2, h1, o) != h2:
            rez[f"RightH2"] = (h1[0],h1[1], o[0],o[1], RightX(h2, h1, o)[0],RightX(h2, h1, o)[1])
        if LeftX(h2, h1, o) != h2:
            rez[f"LeftH2"] = (h1[0],h1[1], o[0],o[1], LeftX(h2, h1, o)[0],LeftX(h2, h1, o)[1])
        if UpX(h2, h1, o) != h2:
            rez[f"UpH2"] = (h1[0],h1[1], o[0],o[1], UpX(h2, h1, o)[0],UpX(h2, h1, o)[1])
        if DownX(h2, h1, o) != h2:
            rez[f"DownH2"] = (h1[0],h1[1], o[0],o[1], DownX(h2, h1, o)[0],DownX(h2, h1, o)[1])
        return rez
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        if state[0]==state[2]==state[4]:
            if (state[1]+1)==state[3] and (state[3]+1)==state[5]:
                return True
        return False
    def h(self,node):
        state=node.state
        counter=0
        if state[0] == state[2]:
            if (state[1] + 1) != state[3]:
                counter+=1
        else:
            counter+=1
        if state[0] == state[4]:
            if (state[1] + 2) != state[5]:
                counter+=1
        else:
            counter+=1
        if state[2]==state[4]:
            if (state[3]+1)!=state[5]:
                counter+=1
        else:
            counter+=1
        return counter



if __name__=='__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [5, 2]
    o_pos = [4, 7]
    h2_pos = [0, 2]
    Molekula=Molecule(obstacles_list,(h1_pos[0],h1_pos[1],o_pos[0],o_pos[1],h2_pos[0],h2_pos[1]))
    rezultat=astar_search(Molekula)
    rez1 = greedy_best_first_graph_search(Molekula)
    rez2 = recursive_best_first_search(Molekula)
    print(rezultat.solution())
    print(rezultat.solve())
    print(rez1.solution())
    print(rez1.solve())
    print(rez2.solution())
    print(rez2.solve())
