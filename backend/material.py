class Material():
    def __init__(self,poisson,elasticidade,identificacao) -> None:
        self._v = poisson
        self._E = elasticidade
        self._nome = identificacao
    def __str__(self) -> str:
        return(f"{self._nome}, poisson={self._v}, elasticidade={self._E}")
    def get_E(self):
        return(self._E)
    def get_v(self):
        return(self._v)
    def get_identificacao(self):
        return(self._nome)
