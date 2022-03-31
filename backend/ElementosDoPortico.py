import math
import numpy

#Variáveis
nodes = [[0,0],[0,4],[4,4],[4,0]]
barras=[[0,1],[1,2],[2,3]]
elasticidade = [2.1e8,2.1e8,2.1e8]
area = [0.5e-2,0.5e-2,0.5e-2]
inercia = [4e-4,4e-4,4e-4]
engaste = [3,3,3]

class ElementosDoPortico():
    def __init__(self) -> None:
        """Classe que define e interpreta os elementos do pórtico"""
        pass
    def material_elemento(self,E:list,I:list,A:list,engaste:list,pontos:list,elementos:list)->list:
        prop_material=[]
        comprimento = self.comprimento_elemento(pontos,elementos)
        for i in range(len(engaste)):
            a = []
            a.append(E[i])
            a.append(I[i])
            a.append(A[i]) 
            a.append(engaste[i]) 
            a.append(comprimento[i])
            prop_material.append(a)
        return(prop_material)
    def definir_elemento(self,pontos:list,elementos:list)->list:
        ligacoes = []

        for i in elementos:
            comp_x = math.fabs(pontos[i[1]][0] - pontos[i[0]][0])
            comp_y = math.fabs(pontos[i[1]][1] - pontos[i[0]][1])
            ligacoes.append([comp_x,comp_y])
 
        return(ligacoes)
    def angulo_elemento(self,pontos:list,elementos:list)->list:
        ligacoes = self.definir_elemento(pontos,elementos)
        angulo = []
        for i in ligacoes:
            if(i[0] == 0):
                angulo.append(90)
            elif(i[1] == 0):
                angulo.append(0)
            else:
                angulo.append("Erro")
        
        return(angulo)
    def comprimento_elemento(self,pontos:list,elementos:list)->list:
        ligacoes = self.definir_elemento(pontos,elementos)
        comprimento = []
        for i in ligacoes:
            if(i[0] == 0):
                comprimento.append(math.fabs(i[1]))
            elif(i[1] == 0):
                comprimento.append(math.fabs(i[0]))
            else:
                comprimento.append("Erro")
        
        return(comprimento)
class CalculoPorticoPlano():
    def __init__(self) -> None:
        """Classe que faz os cálculos de momento fletor e reações do pórtico
        OBS:
        1. Calcula apenas pórtico plano
        2. Calcula apenas situações de engaste 
        3. Considera flexão, cortante e normal
        """
        pass
    def rotacao_coord_local(self,elemento_angulo:list)->list:
        n = 0 
        ang_radians = []
        for i in elemento_angulo:
            ang_radians.append(math.radians(i))

            if(i==90):
                n+=1

        a = numpy.zeros((n**2)*9).reshape(n*3,n*3)
       
        matrizes_rotacao = []
        for ang in ang_radians:
            b=0
            c=0

            #Padrao para o plano com 3 coordenadas
            r = numpy.array([[math.cos(ang),math.sin(ang),0],
                            [-math.sin(ang),math.cos(ang),0],
                            [0,0,1]], dtype="int")
            
            for k in range(n):
                c+=3
                for i in range(b,c):             
                    for j in range(b,c):
                        a[i][j] = r[i-b][j-b]
                b=c
            matrizes_rotacao.append(a.copy())
            
        return(matrizes_rotacao)
    def rigidez_local(self,prop_material) -> list:
        a = []
        b = []
        L = []
        matriz_geral = []

        for i in range(len(prop_material)):
            a.append(prop_material[i][0]*prop_material[i][2]/prop_material[i][4])
            b.append(prop_material[i][0]*prop_material[i][1]/prop_material[i][4])
            L.append(prop_material[i][4])

        

            if(prop_material[i][3] == 3):
                r = numpy.array([[a[i],0,0,-a[i],0,0],
                                [0,12*b[i]/L**2,6*b/L,0,-12*b[i]/L**2,6*b[i]/L],
                                [0,6*b[i]/L,4*b[i],0,-6*b[i]/L,2*b[i]],
                                [-a[i],0,0,a[i],0,0],
                                [0,-12*b[i]/L**2,-6*b[i]/L,0,12*b[i]/L**2,-6*b[i]/L],
                                [0,6*b[i]/L,2*b[i],0,-6*b[i]/L,4*b[i]]])
                matriz_geral.append(r)
        

portico = ElementosDoPortico()     
portico_calculo = CalculoPorticoPlano()
portico_calculo.rigidez_local(portico.material_elemento(elasticidade,inercia,area,engaste,nodes,barras))
#print(portico_calculo.rotacao_coord_local(portico.angulo_elemento(nodes,barras)))

          
            
            

        
