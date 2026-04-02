from searching_framework import Problem, astar_search

moves={"Wait":(0,0),"Up 1":(0,1),"Up 2":(0,2),"Up-right 1":(1,1),"Up-right 2":(2,2),"Up-left 1":(-1,1),"Up-left 2":(-2,2)}

class Climb(Problem):
    def __init__(self,allowed,initial,goal=None):
        super().__init__(initial,goal)
        self.allowed=set(allowed)

    def check_valid(self,state):
        (mx,my),(hx,hy),hd=state
        m_pos=(mx,my)
        c_allowed=self.allowed
        c_allowed.add((hx,hy))
        if not m_pos in c_allowed or not 0<=mx<5 or not 0<=my<9:
            c_allowed.remove((hx,hy))
            return False
        c_allowed.remove((hx,hy))
        return True
    def successor(self, state):
        rez={}
        (mx,my),(hx,hy),hd=state
        if hx==4:
            hd="left"
        elif hx==0:
            hd="right"
        if hd=="right":
            nhx=hx+1
        else:
            nhx=hx-1
        for action,(dx,dy) in moves.items():
            n_pos=(mx+dx,my+dy)
            n_h_pos=(nhx,hy)
            if self.check_valid((n_pos,n_h_pos,hd)):
                rez[action]=(n_pos,n_h_pos,hd)
        return rez
    def actions(self, state):
        return self.successor(state)
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        m,h,hd=state
        return m==h
    def h(self,node):
        (mx,my),(hx,hy),hd=node.state
        # return (abs(mx-hx)+abs(my-hy))/2
        if abs(mx-hx)//2 > abs(my-hy)//2:
            print("Da")
        return abs(my-hy)/2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    # your code here
    man_pos=tuple(map(int,input().split(',')))
    house_pos=tuple(map(int,input().split(',')))
    hous_dir=input()
    problem=Climb(allowed,(man_pos,house_pos,hous_dir))

    rezultat=astar_search(problem)
    if rezultat:
        print(rezultat.solution())
    else:
        print("No Solution!")