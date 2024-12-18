#pensar en casos bordes
def max_paneles(x,y,a,b):
    i=0
    contador = 0
    while x-i>=b:
        j=0
        while y-j>=a:
            j+=a 
            contador +=1
        i+=b
    ##preguntar si puedo colocarlos acostados
    print(j,i)
    new_j=0
    while x-i>=a:
        j=new_j
        while y-j>=b:
            j+=b
            contador+=1
        i+=a
    return contador       
print(max_paneles(2,4,1,2))
print(max_paneles(3,5,1,2))
print(max_paneles(1,10,2,2))