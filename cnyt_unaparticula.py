#Sistema cuántico de partícula en una línea
#Autor: Julian Camacho

import Proyecto_terminado as pt

def probabilidad_particula_estado_x(v,k):
    """(list, int) -> int
    El sistema debe calcular la probabilidad de
    encontrarlo en una posición en particular."""
    c = 0
    
    for i in v:
        c = c + (pt.modulo(i))** 2
        
    return(round(100*pt.modulo(v[k])**2/c,3))

def AmplitudTransicion(v_one, v_two):
    """(list, list) -> list
     El sistema si se le da otro vector Ket debe
    buscar la probabilidad de transitar del primer
    vector al segundo."""
    
    v_p_v = pt.producto_interno(v_two,v_one)
    pro_normas = pt.multi([pt.norma_vector(v_one), 0],[pt.norma_vector(v_two), 0])
    pro_normas[0] = 1/pro_normas[0]
    
    return pt.multi(pro_normas, v_p_v)


def main():
                    
    v_one = [[2,1],[-1,2],[0,1],[1,0],[3,-1],[2,0],[0,-2],[-2,1],[1,-3],[0,-1]]
    v_two = [[-1,-4],[2,-3],[-7,6],[-1,1],[-5,-3],[5,0],[5,8],[4,-4],[8,-7],[2,-7]]

    i = [[1,0],[0,-1]]
    j = [[0,1],[1,0]]

    m = [[ [2,0] , [1,1]],[[1,-1], [3,0]] ]
    v = [[1/(2)**0.5,0],[0,1/(2)**0.5]]
    

    print(probabilidad_particula_estado_x(v_one,7))
    print(AmplitudTransicion(v_one, v_two))

main()
