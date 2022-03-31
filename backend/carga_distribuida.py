class CargaDistribuida():
    def __init__(self,qx,qy,nome) -> None:
        self._qx = qx
        self._qy = qy
        self._nome = nome
    def __str__(self) -> str:
        return(f"C{self._nome}={self._qx},{self._qy}")
    def set_barra_carga_distribuida(self,barra):
        self._barra=barra
    def get_barra_carga_distribuida(self):
        return(self._barra)
    def get_qx(self):
        return(self._qx)
    def get_qy(self):
        return(self._qy)
    def get_id(self):
        return(self._nome)