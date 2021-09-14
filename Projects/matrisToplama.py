# -*- coding: utf-8 -*-

matris1 = [[1,3,4],[6,8,1],[4,0,8]]
matris2 = [[2,5,3],[4,3,5],[1,2,3]]

sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matris1)):
    for j in range(len(matris2)):
      
        sonuc[i][j] = matris1[i][j]+matris2[i][j]
        
print(sonuc)        
# for i in range(1,4):
#     sonuc = matris1[] + matris2[]
#     print(sonuc)