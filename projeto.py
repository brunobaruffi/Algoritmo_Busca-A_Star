import math
import matplotlib.pyplot as plt

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
        self.vetorCaminhoFinal = []

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
                math.fabs(math.pow(x-x0,2)) + 
            math.fabs(math.pow(y-y0,2))
            )
        return round(dist,3)

    def avaliarVizinhosEVetorAbarto(self, vizinhos, posisaoVetorFechado):
        Controle = 999999
        semVizinho = False
        vetorControle = []
        posControle = 0
        #Rodar todos os vizinhos enviados, adicionar no vetorControle 
        #validando a distanca.
        c=0
        for i in vizinhos:
            tempDistancia = self.verificarDistanciaXY(i[0],i[1],self.fimx,self.fimy)
            vetorControle.append([i[0],i[1],posisaoVetorFechado,tempDistancia])
            
            if (c == 0):
               Controle = tempDistancia
            else:
                if(tempDistancia<Controle):
                    Controle = tempDistancia
                    posControle = c
            c = c + 1
        #Validando o vetorAberto, buscando o mais proximo deles
        c=0
        for i in self.vetorAberto:
            if (i[3] < Controle):
                semVizinho = True
                Controle = i[3]
                posControle = c
            c = c + 1 
        
        #redefinição dos vetores aberto e fechado
        addVetorFechado = []
        if(semVizinho == True):
            addVetorFechado.append(self.vetorAberto[posControle])
            del self.vetorAberto[posControle]
        else:
            addVetorFechado.append(vetorControle[posControle])
            del vetorControle[posControle]
            
        self.vetorFechado.append(addVetorFechado[0])
        for i in vetorControle:
            self.vetorAberto.append(i)
            
    def buscarCaminho(self):
        self.vetorFechado.append([self.iniciox, self.inicioy, 0, self.verificarDistanciaXY(self.iniciox, self.inicioy, self.fimx, self.fimy)])
        saida = 0
        while saida == 0:
            if (self.vetorFechado == 0):
                saida = 1
            else:
                x = self.vetorFechado[-1][0]
                y = self.vetorFechado[-1][1]
                posisaoVetorFechado = len(self.vetorFechado) - 1
                vizinhos = self.verNovosVizinhos(x, y)
                
                self.avaliarVizinhosEVetorAbarto(vizinhos,posisaoVetorFechado)
                
                if(self.vetorFechado[-1][3] > 0):
                    saida = 0
                else:
                    saida = 1
        
        self.gerarCaminhoFinal()
        self.gerarGrafico()

        
    def gerarCaminhoFinal(self):
       fechado = self.vetorFechado
       fechado.reverse()
       self.vetorCaminhoFinal.clear()
       c=0
       for i in fechado:
          if(c==0):
              self.vetorCaminhoFinal.append([i[0],i[1],i[2],i[3]])
          else:
              if(i[2] != 0):
                  self.vetorCaminhoFinal.append([i[0],i[1],i[2],i[3]])
              else:
                  self.vetorCaminhoFinal.append([i[0],i[1],i[2],i[3]])
                  break
          c = c + 1
       fechado.reverse()
       self.vetorCaminhoFinal.append([fechado[0][0],fechado[0][1],fechado[0][2],fechado[0][3]])   
       self.vetorCaminhoFinal.reverse()
       
    def gerarGrafico(self):
        plt.xlim(0,self.tamanhoY + 2)
        plt.ylim(0,self.tamanhoX + 2)
        corpo = self.corpo
        for i in self.vetorCaminhoFinal:
            corpo[i[0]][i[1]] = "X"
            
        c=1
        corpo.reverse()
        for i in corpo:
            d=1
            for j in i:
                if(j == 1):
                    cor = 'blue'
                elif(j == 0):
                    cor = 'grey'
                elif(j == "X"):
                    cor = 'green'
                plt.text(d, c, j, backgroundcolor=cor)
                d= d + 1
            c = c + 1
        plt.show()
            
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
chamada.buscarCaminho()
print(chamada.vetorCaminhoFinal)
#print(chamada.vetorFechado)
#print(chamada.vetorAberto)