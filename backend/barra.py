from backend.no import *
from backend.carga_distribuida import *
from backend.seccao import *
from backend.material import *
from math import radians,atan,cos,sin
import numpy

class Barra():
    def __init__(self,no_i:No,no_f:No,id) -> None:
        self._no_i = no_i
        self._no_f = no_f
        self._id = id
    def __str__(self) -> str: 
        return(f"Barra {self._id }[i({self._no_i}),f({self._no_f})]")
    def set_seccao(self,seccao:Seccao):
        self._seccao = seccao
    def set_material(self,material:Material):
        self._material = material
    def set_carga_distribuida(self,carga:CargaDistribuida):
        self._carga = carga
    def get_inicio_barra(self):
        return(self._no_i)
    def get_final_barra(self):
        return(self._no_f)
    def get_id(self):
        return(self._id)
    def get_L(self):
        x0 = self._no_i.get_x()
        y0 = self._no_i.get_y()
        x1 = self._no_f.get_x()
        y1 = self._no_f.get_y()
        distancia = ((x0-x1)**2+(y0-y1)**2)**0.5
        return(distancia)
    def get_angulo(self):
        x0 = self._no_i.get_x()
        y0 = self._no_i.get_y()
        x1 = self._no_f.get_x()
        y1 = self._no_f.get_y()

        if((x0-x1) == 0):
            angulo = radians(90)
        elif((y0-y1) == 0):
            angulo = radians(0)
        else:
            angulo = atan((y0-y1)/(x0-x1))
        return(angulo)
    def get_seccao(self):
        return(self._seccao)
    def get_material(self):
        return(self._material)
    def get_matriz_rotacao(self):
        ang = self.get_angulo()
       
        #Padrao para o plano com 3 coordenadas
        r = numpy.array([[cos(ang),sin(ang),0,0,0,0],
                        [-sin(ang),cos(ang),0,0,0,0],
                        [0,0,1,0,0,0],
                        [0,0,0,cos(ang),sin(ang),0],
                        [0,0,0,-sin(ang),cos(ang),0],
                        [0,0,0,0,0,1]], dtype="int")
            
        return(r.copy())
    def get_ke_local(self):
        a = self._seccao.get_area()*self._material.get_E()/self.get_L()
        b = self._material.get_E()*self._seccao.get_inercia()/self.get_L()
        L = self.get_L()

        if(self._no_i.get_vinculacao().get_vinculacao_type() == self._no_f.get_vinculacao().get_vinculacao_type() == 2):
            u = numpy.array([[a,0,0,-a,0,0],
                            [0,12*b/L**2,6*b/L,0,-12*b/L**2,6*b/L],
                            [0,6*b/L,4*b,0,-6*b/L,2*b],
                            [-a,0,0,a,0,0],
                            [0,-12*b/L**2,-6*b/L,0,12*b/L**2,-6*b/L],
                            [0,6*b/L,2*b,0,-6*b/L,4*b]])
            
            if(self.get_angulo() == radians(0)):
                r = u
               
            elif(self.get_angulo() != radians(0)):
                r = self.get_matriz_rotacao().transpose()@u@self.get_matriz_rotacao()
                
                
        else:
            r = "Só está definido vinculo do terceiro gênero"
        return(r)