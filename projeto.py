
class buscar_labirinto:
    
    def __init__(self, corpo, inicio, fim):
        self.corpo = corpo
        self.iniciox = inicio[0]
        self.inicioy = inicio[1]
        self.fimx = fim[0]
        self.fimy = fim[1]
        self.vetorFechado = []
        self.vetorAberto = []
        




    def verNovosVizinhos(self, x, y):
        #x+1,y-1
        #x+1,y
        #x+1,y+1
        
        #x,y+1
        #x,y-1
        
        #x-1,y-1
        #x-1,y
        #x-1,y+1
        
        #if(self.corpo[x+1,y])
        #print (self.fimx)
        #self.vetorAberto.append([3,2,1,12])
        temp = self.verificarVetorAberto(x,y)
        print (temp)

    def verificarExistenciaVetorAberto(self,x,y):
        for i in self.vetorAberto:
            if((i[0] == x) and (i[1] == y)):
                return True
        return False
    
    def verificarExistenciaVetorFechado(self,x,y):
        for i in self.vetorFechado:
            if((i[0] == x) and (i[1] == y)):
                return True
        return False 
    


#-------------------corpo principal!-----------------------------

#Vetor corpo composto pela distancia e um vetor dos vizinhos.
corpo = [  # 0,1,2,3,4,5,6,7
            [1,1,1,1,0,1,1,1], # 0
            [1,0,0,0,0,1,1,1], # 1
            [1,1,1,1,0,1,1,1], # 2
            [1,1,1,1,1,1,1,1]  # 3
        ]
#indica o ponto de partida do vetor
inicio = [0,0]
#indica o ponto final de chegada
final = [7,0]


chamada = buscar_labirinto(corpo, inicio, final)

chamada.verNovosVizinhos(3, 3)                        















#while posicao != final:
 



#for d in range(len(corpo)):
 #   print(corpo[d])
  #  pass



#for c in corpo:
    #print(c)    
 #   pass
    

