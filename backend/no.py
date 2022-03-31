from backend.forca_nodal import *
from backend.vinculacoes import *

class No():
    def __init__(self,x=0,y=0,id=0):
        self._x = x
        self._y = y
        self._id = id
    def __repr__(self) -> str:
        return(f"No{self._id}({self._x},{self._y})")
    def __str__(self) -> str:
        return(f"No{self._id}({self._x},{self._y})")
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_id(self):
        return self._id
    def set_vinculacao(self,vinculacao:Vinculacoes):
        self._vinculacao = vinculacao
    def get_vinculacao(self):
        return(self._vinculacao)
    def set_forca(self,forca:Forca):
        self._forca = forca
    def get_forca(self):
        return(self._forca)

        
        
    
        

    