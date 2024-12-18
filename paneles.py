#Asumimos que los rectangulos en un principio se colocan de la forma
#              _______                  
#             |       |                          
#             |       | a           
#             |       |             
#             |_______|  
#                 b          
#Donde x es el largo, e y es el alto

#Funcion que rellena el cuadrado xy con cuadrado cuadrados de ab
def recorrer_cuadrado(x,y,a,b,contador):
    i=0
    j=0
    while x-i>=b:
        j=0
        while y-j>=a:
            j+=a 
            contador +=1
        i+=b
    return (i,j,contador)

#Funcion que retorna el maximo numero de cuadrados de dimensiones ab que caben dentro de un
#cuadrado de dimensiones xy
def max_paneles(x,y,a,b):
    contador = 0
    if a==0 or b==0 or x==0 or y==0:
        print("dimensiones invalidas")
        return 0
    #casos cuando hay que rotar el cuadrado de axb inmediatamente
    if b>x:
        _,_,contador = recorrer_cuadrado(x,y,b,a,contador)
        return contador
    elif a>y:
        _,_,contador = recorrer_cuadrado(x,y,b,a,contador)
        return contador
    elif a>y and b>x:
        print("no se puede colocar este cuadrado, dimensiones mas grandes que el molde")
        return
    i,j,contador=recorrer_cuadrado(x,y,a,b,contador)
    contador_2 = contador
    #En esta parte puede que haya que llenar para x-i*b X j*a y  b*i X y-j*a. Pero no sé cual es mejor, tendremos que 
    # escoger el par que entregue un numero mayor, y si son iguales, entonces no hay problema    
    aj = j
    y2 = y - aj
    bi= i
    #estamos viendo x X y-j*a
    i,j,contador=recorrer_cuadrado(x,y2,b,a,contador)
    #vamos a revisar x-i*b X j*a
    x2 = x - bi
    i,j,contador=recorrer_cuadrado(x2,y-y2,b,a,contador)
    #caso cuando se rellena y primero
    i,j,contador_2=recorrer_cuadrado(x2,y,b,a,contador_2)
    #vamos a revisar x-i*b X y - j*a
    x2 = x - bi
    i,j,contador_2=recorrer_cuadrado(x-x2,y2,b,a,contador_2)
    if contador>contador_2:
        return contador
    else:
        return contador_2

if __name__ == '__main__':   
    print(max_paneles(4,2,2,1))
    print(max_paneles(5,3,2,1))
    print(max_paneles(10,1,2,2))
    print(max_paneles(7,16,5,8))
    max_paneles(2,15,0,0)
    max_paneles(2,0,1,1)
    print(max_paneles(10,15,6,1))
    print(max_paneles(10,15,1,4))
