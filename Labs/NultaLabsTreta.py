
class Robot:
    def __init__(self,x,y,direction):
        self.r=x
        self.c=y
        self.direction=direction
    def turn(self):
        if self.direction== 'up':
            self.direction='right'
        elif self.direction== 'right':
            self.direction='down'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'up'
    def move(self,grid):
        counter=0
        if self.direction== 'up':
            if (self.r-1)<0:
                self.turn()
                return 0
            elif grid[self.r-1][self.c]=='#':
                self.turn()
                return 0
            elif grid[self.r-1][self.c]=='.':
                grid[self.r-1][self.c]='c'
                self.r=self.r-1
                counter+=1
                counter+=self.move(grid)
            else:
                self.r = self.r - 1
                counter += self.move(grid)
        elif self.direction== 'down':
            if (self.r + 1) >=len(grid):
                self.turn()
                return 0
            elif grid[self.r+1][self.c] == '#':
                self.turn()
                return 0
            elif grid[self.r+1][self.c] == '.':
                grid[self.r+1][self.c] = 'c'
                self.r = self.r + 1
                counter += 1
                counter += self.move(grid)
            else:
                self.r = self.r + 1
                counter += self.move(grid)
        elif self.direction == 'right':
            if (self.c + 1) >= len(grid[0]):
                self.turn()
                return 0
            elif grid[self.r][self.c+1] == '#':
                self.turn()
                return 0
            elif grid[self.r][self.c+1] == '.':
                grid[self.r][self.c+1] = 'c'
                self.c = self.c + 1
                counter += 1
                counter += self.move(grid)
            else:
                self.c = self.c + 1
                counter += self.move(grid)
        elif self.direction == 'left':
            if (self.c - 1) < 0:
                self.turn()
                return 0
            elif grid[self.r][self.c-1] == '#':
                self.turn()
                return 0
            elif grid[self.r][self.c-1] == '.':
                grid[self.r][self.c-1] = 'c'
                self.c = self.c - 1
                counter += 1
                counter += self.move(grid)
            else:
                self.c = self.c - 1
                counter += self.move(grid)
        return counter
class Game:
    def __init__(self,r1,c1,dir1,r2,c2,dir2):
        self.grid=[['#', '.', '.', '#', '.', '.'], ['.', '#', '.', '.', '.', '.'], ['#', '.', '.', '.', '.', '.'],
                ['.', '#', '.', '.', '.','.'], ['.', '.', '.', '#', '.', '.']]
        self.r1=Robot(int(r1),int(c1),dir1)
        self.r2=Robot(int(r2),int(c2),dir2)
        self.grid[int(r1)][int(c1)]='c'
        self.grid[int(r2)][int(c2)]='c'

x1,y1,dir1=input().split()
x2,y2,dir2=input().split()

Igra = Game(x1,y1,dir1,x2,y2,dir2)
counter=0
for i in range(15):
    counter+=Igra.r1.move(Igra.grid)
    counter+=Igra.r2.move(Igra.grid)
print(counter+2)