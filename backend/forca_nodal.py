class Forca():
    def __init__(self,identificacao,forc_x,forc_y,m) -> None:
        self._identificacao=identificacao
        self._forc_x=forc_x
        self._forc_y = forc_y
        self._m = m
    def __str__(self) -> str:
        return(f"F{self._identificacao}={self._forc_x}x,{self._forc_y}y, {self._m}m")
    def __repr__(self):
        return(f"F{self._identificacao}={self._forc_x}x,{self._forc_y}y, {self._m}m")
    def get_forc_x(self):
        return(self._forc_x)
    def get_forc_y(self):
        return(self._forc_y)
    def get_m(self):
        return(self._m)
    def get_id(self):
        return(self._identificacao)
 