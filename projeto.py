import math

class buscar_labirinto:
    
    def __init__(self, corpo, inicio, fim, tamanho):
        self.corpo = corpo
        self.iniciox = inicio[0]
        self.inicioy = inicio[1]
        self.fimx = fim[0]
        self.fimy = fim[1]
        self.tamanhoX = tamanho[0]  #linhas
        self.tamanhoY = tamanho[1]  #colunas
        self.vetorFechado = []
        self.vetorAberto = []
                
        #self.vetorAberto.append([3,2,1,12])
        #self.vetorFechado.append([2,2,1,12])



    def verNovosVizinhos(self, x, y):
        saida = []
        #O algoritmo abaixo verifica todos os 8 vizinhos 

        #x+1,y-1
        if ((y-1 >= 0) and (x+1 <= self.tamanhoX)):
            if(self.corpo[x+1][y-1] == 1):               
                if (self.verificarExistenciaVetorAberto(x+1, y-1) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y-1) == False):
                        saida.append([x+1,y-1])                     
        #x+1,y
        if ((x+1 <= self.tamanhoX)):
            if(self.corpo[x+1][y] == 1):
                if (self.verificarExistenciaVetorAberto(x+1, y) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y) == False):
                        saida.append([x+1,y])
        #x+1,y+1
        if ((y+1 <=self.tamanhoY) and (x+1 <= self.tamanhoX)):
            if(self.corpo[x+1][y+1] == 1):
                if (self.verificarExistenciaVetorAberto(x+1, y+1) == False):
                    if(self.verificarExistenciaVetorFechado(x+1, y+1) == False):
                        saida.append([x+1,y+1])       
        #x,y+1
        if ((y+1 <=self.tamanhoY)):
            if(self.corpo[x][y+1] == 1):
                if (self.verificarExistenciaVetorAberto(x, y+1) == False):
                    if(self.verificarExistenciaVetorFechado(x, y+1) == False):
                        saida.append([x,y+1])
        #x,y-1
        if ((y-1 >=0)):
            if(self.corpo[x][y-1] == 1):
                if (self.verificarExistenciaVetorAberto(x, y-1) == False):
                    if(self.verificarExistenciaVetorFechado(x, y-1) == False):
                        saida.append([x,y-1])       
        #x-1,y-1
        if ((y-1 >= 0) and (x-1 >= 0)):
            if(self.corpo[x-1][y-1] == 1):
                if (self.verificarExistenciaVetorAberto(x-1, y-1) == False):
                    if(self.verificarExistenciaVetorFechado(x-1, y-1) == False):
                        saida.append([x-1,y-1])
        #x-1,y
        if ((x-1 >= 0)):
            if(self.corpo[x-1][y] == 1):
                if (self.verificarExistenciaVetorAberto(x-1, y) == False):
                    if(self.verificarExistenciaVetorFechado(x-1, y) == False):
                        saida.append([x-1,y])
        #x-1,y+1
        if ((y+1 <= self.tamanhoY) and (x-1 >= 0)):
            if(self.corpo[x-1][y+1] == 1):
                if (self.verificarExistenciaVetorAberto(x-1, y+1) == False):
                    if(self.verificarExistenciaVetorFechado(x-1, y+1) == False):
                        saida.append([x-1,y+1])
                      
        return saida

    def verificarExistenciaVetorAberto(self,x,y):
        #Roda o vetor aberto conferindo se o x,y esta la
        for i in self.vetorAberto:
            if((i[0] == x) and (i[1] == y)):
                return True
        return False
    
    def verificarExistenciaVetorFechado(self,x,y):
        #Roda o vetor fechado conferindo se o x,y esta la
        for i in self.vetorFechado:
            if((i[0] == x) and (i[1] == y)):
                return True
        return False 
    
    def verificarDistanciaXY(self,x0,y0,x,y):
        #Calcula a distancia euclidiana entre duas coordenadas,
        #utilizando a formula de pitagoras.
        dist = math.sqrt(
            round(
                math.fabs(math.pow(x-x0,2))) + 
            round(math.fabs(math.pow(y-y0,2)))
            )
        return dist


#-------------------corpo principal!-----------------------------

#Vetor corpo composto pela distancia e um vetor dos vizinhos.
corpo = [  # 0,1,2,3,4,5,6,7
            [1,1,1,1,0,1,1,1], # 0
            [1,0,0,0,0,1,1,1], # 1
            [1,1,1,1,0,1,1,1], # 2
            [1,1,1,1,1,1,1,1]  # 3
        ]
#Tamanho de x,y(linhas e colunas)
tamanho = [3,7]
#indica o ponto de partida do vetor
inicio = [0,0]
#indica o ponto final de chegada
final = [0,7]


chamada = buscar_labirinto(corpo, inicio, final, tamanho)

#print(chamada.verNovosVizinhos(2, 3))

#print(chamada.verificarDistanciaXY(0, 0, 3, 4))













#while posicao != final:
 



#for d in range(len(corpo)):
 #   print(corpo[d])
  #  pass



#for c in corpo:
    #print(c)    
 #   pass
    

