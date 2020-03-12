#Operaciones con vectores y matricen en los complejos
#Autor: Julian Camacho
#Enero de 2019

import sys
import math

#--------------------------------------------------------------------------------
#---------------------------- Operaciones numeros complejos -----------------------------
#--------------------------------------------------------------------------------

def suma(cu, cd):   
    """(list, list) -> list 
    Suma entre dos numeros complejos"""

    a = cu[0] + cd[0]
    b = cu[1] + cd[1] 
    r= [a,b]
    
    return r

def multi(cu, cd):  
    """(list, list) -> list 
    Producto entre dos numeros complejos"""

    a = cu[0]*cd[0] - cu[1]*cd[1]
    b =  cu[0]*cd[1] + cu[1]*cd[0]
    a = round(a,3)
    b = round(b,3)
    r = [a,b]
    
    return r

def resta(cu, cd): 
    """(list, list) -> list 
    Resta entre dos numeros complejos"""
    
    a = cu[0] - cd[0]
    b = cu[1] - cd[1]
    r= [a,b]
    
    return r

def  cociente(cu, cd):
    """(list, list) -> list 
    Cociente entre dos numeros complejos"""

    a = (cu[0]*cd[0] + cu[1]*cd[1]) / (cu[1] ** 2 + cd[1] ** 2 )
    b = (cu[1]*cd[0] - cu[0]*cd[1]) / (cu[1] ** 2 + cd[1] ** 2)
    r = [a,b]

    return r

def modulo(c):
    """(list) -> list 
    Modulo de un número complejo"""

    r = (c[0] ** 2 + c[1] ** 2) ** 0.5

    return r

def conju(c):
    """(list) -> list 
    Conjugado de un número complejo"""
    
    r = [c[0], c[1] * -1]

    return r

def polares(c):
    """(list) -> list 
    Dado un numero complejo (Representacion en coordenadas cartecianas)
    se convertira a cordenadas polares de la forma (p,o°)"""

    p = (c[0] ** 2 + c[1] ** 2) ** 0.5
    gra = math.atan2(c[1],c[0])
    r = [p, gra]
    
    return r

def fase_complex(c):
    """(list) -> list
    Fase de un numero complejo"""

    fase = math.atan2(c[1],c[0])

    return fase

def inverso(c):
    """(list) -> list
    Inverso aditivo de un numero complejo"""
    r = []
    for i in c:
        r = r + [-i]

    return r
    


#-----------------------------------------------------------------------------------
#--------------------------- Operaciones Vectores complejos-------------------------
#-----------------------------------------------------------------------------------


def suma_vectores(v_one, v_two):
    """(list, list) -> list
    Adición de vectores complejos"""

    r = []
    for i in range(len(v_one)):
        r = r + [suma(v_one[i], v_two[i])]

    return r

def inverso_vecom (v):
    """(list) -> list
    Inverso (aditivo) de un vector complejo"""

    r = []
    for i in v:
        f = []
        for j in i:
            f = f + [-j]
        r = r + [f]
        
    return r

def mult_vector_esca (c, v):
    """(list, list) -> list
    Multiplicación de un escalar por un vector complejo."""

    r = []
    for i in v:
        r = r + [multi(c, i)]
        
    return r

def conjugada_vector(v):
    """(list, list) -> list
    Conjugada de un vector"""

    v_conju=[]

    for i in v:
        v_conju.append(conju(i))

    return v_conju
    

def producto_interno(v_one, v_two):
    """(list, list) -> list
    Producto interno de dos vectores"""

    r = [0,0]
    v_adjunto= conjugada_vector(v_one)

    for j in range(len(v_two)):
        r = suma(r, multi(v_two[j], v_adjunto[j]))

    return r

def norma_vector(v):
    """(list) -> list
    Norma de un vector"""
    
    r = producto_interno(v,v)
    norma = r[0] **(1/2)

    return norma

def distancia_vectores(v_one,v_two):
    """(list, list) -> list
    Distancia entre dos vectores"""
    
    r = norma_vector(suma_vectores(v_one, inverso_vecom(v_two)))
    return r


    
#---------------------------------------------------------------------------------
#--------------------- Operacion Matrices complejas ------------------------------
#---------------------------------------------------------------------------------
    

def suma_matrices(m_one, m_two):
    """(list,list) -> list
    Adición de matrices complejas"""

    r = []
    for i in range(len(m_one)):
        r = r + [suma_vectores(m_one[i], m_two[i])]

    return r

def inver_matrix(m):
    """(list) -> list
    Inversa (aditiva) de una matriz compleja"""

    r = []
    for i in m:
        r = r + [inverso_vecom(i)]

    return r

def matrix_escalar(c, m):
    """(list, list) -> list
    Multiplicación de un escalar por una matriz compleja"""

    r = []
    for i in m:
        r = r + [mult_vector_esca(c,i)]
        
    return r

def matrix_trans(m):
    """(lista) -> list
    Transpuesta de una matriz"""

    n = len(m)
    r = []
    for i in range(n):
        f = []

        for j in range(n):
            f = f + [m[j][i]]
        r = r + [f]
        
    return r

def matrix_conjugada(m):
    """(list) -> list
    Conjugada de una matriz"""

    r = []
    for i in m:
        f = []
        for j in i:
            f = f + [conju(j)]
        r = r + [f]
        
    return r

def matriz_adjunta(m):
    """(list) -> list
    Adjunta de una matriz"""
    r = matrix_conjugada(matrix_trans(m))
    return r

def producto_matrix(m_one, m_two):
    """(list, list) ->  list
    Multiplicacion de matrices"""

    if len(m_one[0]) == len(m_two):

        r = [[[0,0] for i in range (len(m_one))] for j in range (len(m_two[0]))]

        for i in range (len(m_one)):
            for j in range(len(m_two[0])):
                for k in range(len(m_two)):
                    r[i][j] = suma(r[i][j], multi( m_one[i][k],m_two[k][j]))

                
        return (r)

    else:
        print("Dimension incopatibles")



def accion_matrix(m,v):
    """(list, list) -> list
    Accion de un vector sobre una matriz"""

    if len(m[0]) == len(v):
        
        r = [[0,0] for i in range(len(v))]
        
        for i in range(len(m)):
            for k in range(len(v)):
                r[i] = suma(r[i], multi(m[i][k], v[k]))
        return (r)       

    else: 
        print("Dimension incopatibles")

def matriz_unitaria(m):
    """(list, list) -> Boolean
    Revisar si una matriz es unitaria"""
    uni = []
    for i in range(len(m)):
        f = []
        for k in range(len(m)):
            if i == k:
                f = f + [[1,0]]
            else:
                f = f + [[0,0]]
        uni = uni + [f]
    if producto_matrix(m,matriz_adjunta(m)) == producto_matrix(m,matriz_adjunta(m)) and producto_matrix(m,matriz_adjunta(m)) == uni:
        return True
    else:
        return False

def matriz_hermitiana(m):
    """(list, list) -> Boolean
    Revisar si una matriz es Hermitiana"""

    if m == matriz_adjunta(m):
        return True
    else:
        return False
    


def p_tensor(m,n):
    """(list, list) -> list
    Producto tensor de dos matrices"""
    res = []
    control = 0
    pj = 0
    for k in range((len(m)-1)*2):
        f1 = m[k]
        f2 = n[pj]
        f = []        
        for i in f1:
            for j in f2:
                f.append(multi(i,j))        
        pj += 1
        f2 = n[pj]
        res.append(f)
        f = []        
        for i in f1:
            for j in f2:
                f.append(multi(i,j))                
        pj -= 1
        res.append(f)
   
    return res


    
def main():


#numero complejo representado por una lista de dos posiciones
    c_one = [1, -2]
    c_two = [4, 5]

#Vectores complejos son representado por vectores usuales, pero con entradas (elemntos) complejos
    v_one = [[1, 2], [4, -4], [0,1]]
    v_two = [[4, 5], [3, 2], [3, 2]]
    v_thre =[[1,2],[3,4]]

#Matrices complejas son representados por matrices usuales pero sus filas son vectores complejos
    
    m_one = [ [[1, 0] , [3, 4]] , [[3, -4], [-1, 0]] ]
    m_two = [ [[-1, -2] , [-3, -4]] , [[4, -3], [1, 2]] ]

##    print(inverso(c_one))
main()
