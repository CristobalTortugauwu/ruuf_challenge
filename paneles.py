#pensar en casos bordes
def max_paneles(x,y,a,b):
    i=0
    contador = 0
    if a==0 or b==0 or x==0 or y==0:
        print("dimensiones invalidas")
        return 0
    while x-i>=b:
        j=0
        while y-j>=a:
            j+=a 
            contador +=1
        i+=b
    new_j=0
    while x-i>=a:
        j=new_j
        while y-j>=b:
            j+=b
            contador+=1
        i+=a
    return contador    
if __name__ == '__main__':   
    print(max_paneles(2,4,1,2))
    print(max_paneles(3,5,1,2))
    print(max_paneles(1,10,2,2))
    print(max_paneles(2,15,0,0))
    print(max_paneles(2,0,1,1))
