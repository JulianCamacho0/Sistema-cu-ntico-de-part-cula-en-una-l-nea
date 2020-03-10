#Sistemas cuanticos
#Autores: Julian Camacho

import Proyecto_terminado as pt



def probabilidad_particula_estado_x(v,k):

    c = 0
    for i in v:
        c = c + (pt.modulo(i))** 2
        
    return(round(100*pt.modulo(v[k])**2/c,3))

def AmplitudTransicion(v_one, v_two):
    
    v_p_v = pt.producto_interno(v_two,v_one)
    pro_normas= pt.multi([pt.norma_vector(v_one), 0],[pt.norma_vector(v_two), 0])
    pro_normas[0] = 1/pro_normas[0]
    
    return pt.multi(pro_normas, v_p_v)

def valor_esperado(m,v):
    
    ket = pt.accion_matrix(m,v)
    return pt.producto_interno(ket,v)
    
def variancia(m,v):

    d = pt.suma_matrices(m, [[ [-1.5,0] , [0,0]],[[0,0], [-1.5 , 0]] ])
    print(valor_esperado(pt.producto_matrix(d,d),v))
                         
    

def main():
                    
    v_one = [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
    v_two = [[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]
##    print(probabilidad_particula_estado_x(v,7))

    i = [[1,0],[0,-1]]
    j = [[0,1],[1,0]]

    m = [[ [2,0] , [1,1]],[[1,-1], [3,0]] ]
    v = [[1/(2)**0.5,0],[0,1/(2)**0.5]]
##    print(valor_esperado(m,v))
    variancia(m,v)
##    print(AmplitudTransicion(v_one, v_two))

main()
    
