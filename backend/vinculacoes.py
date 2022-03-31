class Vinculacoes():
    def __init__(self,_rest_x,_rest_y,_rest_m):
        self._rest_x = _rest_x
        self._rest_y = _rest_y
        self._rest_m = _rest_m
    def __str__(self) -> str:
        return(f"_rest_x = {self._rest_x}, _rest_y={self._rest_y}, _rest_m={self._rest_m}")
    def __repr__(self) -> str:
        return(f"_rest_x = {self._rest_x}, _rest_y={self._rest_y}, _rest_m={self._rest_m}")
    def get_rest_x(self):
        return(self._rest_x)
    def get_rest_y(self):
        return(self._rest_y)
    def get_rest_m(self):
        return(self._rest_m)
    def get_vinculacao_type(self):
        if(self._rest_x == self._rest_y == self._rest_m == 1):
            vinculacao = 2
        elif(self._rest_x == self._rest_y == 1 and self._rest_m == 0):
            vinculacao = 1
        elif(self._rest_y == 1 and self._rest_m == self._rest_x == 0):
            vinculacao = 0
        return(vinculacao)

        


