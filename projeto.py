#Vetor corpo composto pela distancia e um vetor dos vizinhos.
corpo = [  # 0,1,2,3,4,5,6,7
            [1,1,1,1,0,1,1,1], # 0
            [1,0,0,0,0,1,1,1], # 1
            [1,1,1,1,0,1,1,1], # 2
            [1,1,1,1,1,1,1,1]  # 3
        ]


#indica o ponto de partida do vetor
xinicio = 0
xfinal  = 0
yinicio = 7
yfinal  = 0
#indica o ponto final de chegada
final = 11

#seta a variavel de controle de posiçao atual
#posicao = inicio

#roda ate que a posiçao de controle chegar a ser igual a posiçao final.


class buscar_labirinto:
    
    def __init__(self, corpo, inicio, fim):
        self.corpo = corpo
        self.iniciox = inicio[0]
        self.inicioy = inicio[1]
        self.fimx = fim[0]
        self.fimy = fim[1]




    def verVizinhos(self):
        #print (self.fimx)



chamada = buscar_labirinto(corpo, [0,0], [7,0])
                           
chamada.verVizinhos()














#while posicao != final:
 



#for d in range(len(corpo)):
 #   print(corpo[d])
  #  pass



#for c in corpo:
    #print(c)    
 #   pass
    

