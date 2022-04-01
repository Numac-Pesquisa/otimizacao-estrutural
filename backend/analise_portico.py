from backend.barra import *

class AnalisePortico():
    def __init__(self,*barras:Barra) -> None:
        self._barras = barras
    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    def matriz_rigidez_desmembrada(self):
        n_colunas = self._barras[0].get_ke_local().shape[0]
        n_barras = int(len(self._barras))
        sizeTotal = (n_colunas*n_barras)**2

        a = numpy.zeros(sizeTotal)
        b = a.reshape(n_colunas*n_barras,n_colunas*n_barras)

        var1 = 0
        var2 = 0
        for barra in self._barras:
            var2 = self._barras[0].get_ke_local().shape[0] + var2
            t = barra.get_ke_local()
            for i in range(var2-var1):
                b[i+var1][var1:var2] = t[i]
            var1=var2
        return(b)
    def matriz_incidencia(self):
        
        nos = []
        for barra in self._barras:
            noInicial = barra.get_inicio_barra()
            noFinal = barra.get_final_barra()
            
            if noInicial not in nos:
                nos.append(barra.get_inicio_barra())
            if noFinal not in nos:
                nos.append(barra.get_final_barra())
        
        nLinha = self.matriz_rigidez_desmembrada().shape[0]
        nColuna = (len(nos))*3

        var1 = numpy.zeros(nLinha*nColuna).reshape(nLinha,nColuna)

        sizeNos = len(nos)
        sizeBarras = len(self._barras)
        var2 = 0
        for i in range(sizeNos):
            idBarra = []
          
            for j in range(var2,sizeBarras+var2):
                noI = self._barras[j-var2].get_inicio_barra()
                noF = self._barras[j-var2].get_final_barra()

                if((nos[i] == noI) or (nos[i] == noF)):
                    idBarra.append(self._barras[j-var2].get_id())
                
                for u in range(len(idBarra)):
                    var1[j][j+i*3-var2] = 1
            var2 += 3
        

                

        A = numpy.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,1,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1]])
        
        return(var1)
    def matriz_rigidez_global(self):
        A = self.matriz_incidencia()
        kl = self.matriz_rigidez_desmembrada()
        K = A.transpose()@kl@A
        return(K)


            

            
            


