class Seccao():
    def __init__(self,area,inercia,identificacao) -> None:
        self._A = area
        self._I = inercia
        self._nome = identificacao
    def __str__(self) -> str:
        return(f"{self._nome}, area={self._A}, inercia={self._I}")
    def get_area(self):
        return(self._A)
    def get_inercia(self):
        return(self._I)
    def get_id(self):
        return(self._nome)
    