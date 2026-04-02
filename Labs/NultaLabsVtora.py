

def MineSweeper(lista):
    n=len(lista)
    def CountMines(r,c):
        count=0
        for pr in [-1,0,1]:
            for pc in [-1,0,1]:
                if pr==0 and pc==0:
                    continue
                sr,sc = pr+r,pc+c
                if 0<= sr <n and 0<=sc<n and lista[sr][sc]=='#':
                    count+=1
        return count
    return [
        [lista[r][c] if lista[r][c]=='#' else str(CountMines(r,c)) for c in range(n)]
        for r in range(n)]

n=int(input())
Mapa=[]
for i in range(n):
    podeleno=input().split()
    Mapa.append([a for a in podeleno])
rezultat=MineSweeper(Mapa)
for k in rezultat:
    print('   '.join(k))