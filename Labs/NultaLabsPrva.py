# x=input().split(" ")
# Gradovi={}
# Temperatura={}
# DenoviDozhd={}
# Denovi={}
# while x[0]!= "end":
#     if not(x[0] in Temperatura):
#         Temperatura[x[0]]=float(x[1])
#         Denovi[x[0]] = 1
#         if x[2] == 'yes':
#             DenoviDozhd[x[0]] = 1
#         else:
#             DenoviDozhd[x[0]]=0
#     else:
#         Temperatura[x[0]]+=float(x[1])
#         Denovi[x[0]] += 1
#         if x[2]== 'yes':
#             DenoviDozhd[x[0]]+=1
#     x=input().split(" ")
# for a in Temperatura.keys():
#     if not (a in Gradovi):
#         Gradovi[a]=(a,float((Temperatura[a]/Denovi[a])),int(DenoviDozhd[a]))
# SortiraniGradovi=dict(sorted(Gradovi.items(),key=lambda x:(-x[1][2],x[1][0])))
# # SortiraniGradovi=dict(SortiraniGradovi)
# # print(Gradovi)
# # print(SortiraniGradovi)
# for a in SortiraniGradovi:
#     print(SortiraniGradovi[a][0],end=" ")
#     print(round(SortiraniGradovi[a][1],ndigits=2), end=" ")
#     print(SortiraniGradovi[a][2])

matrix=[[0 for i in range(9)]for a in range(7)]
obstacles = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
for a in obstacles:
    matrix[6-a[1]][a[0]]='#'
print(matrix)