from backend.analise_portico import *

no0 = No(0,0,0)
no1 = No(0,4,1)
no2 = No(4,4,2)
no3 = No(4,0,3)

v0 = Vinculacoes(1,1,1)
f0 = Forca(0,100,0,0)
q0 = CargaDistribuida(0,-10,0)

s0 = Seccao(0.5e-2,4e-4,0)
m0 = Material(0,2.1e8,0)

no0.set_vinculacao(v0)
no0.set_forca(f0)

no1.set_vinculacao(v0)

no2.set_vinculacao(v0)

no3.set_vinculacao(v0)

barra0 = Barra(no0,no1,0)
barra0.set_material(m0)
barra0.set_seccao(s0)

barra1 = Barra(no1,no2,1)
barra1.set_material(m0)
barra1.set_seccao(s0)
barra1.set_carga_distribuida(q0)

barra2 = Barra(no2,no3,2)
barra2.set_material(m0)
barra2.set_seccao(s0)

analise = AnalisePortico(barra0,barra1,barra2)
print(analise.matriz_incidencia())


     