import random 

resultados=[]
datos=[]
r=[random.randint(0,9)]
x=0


def numeroal():
    v=0
    while 3>v:
        aleatorio=random.randint(0,9)
        if aleatorio not in r:
            r.append(aleatorio)
            v=v+1
        
    return r

def  stri(l):
    try: 
        int(l)
        return True
    except ValueError:
        return False
def usuario(l):
    u=[]
    for i in range(len(l)):
        if stri(l):
            d=int(l[i])
        else: return print("Solo deben de ir numeros")
        if d not in u:
            u.append(d)
        else: return print("Ingresaste un número repetido")       
    return u
lis=numeroal()
    
def compara(l):
    datos=[]
    p=0
    for n in range(len(l)):
        for i in range(len(lis)):
            if l[n]==lis[i]:
                    if n==i:
                        datos.insert(0,"*")
                        p=p+1
                        if p==4:
                            return print("Adivinaste el número: ",lis)
                    else:
                        datos.insert(len(datos),"-")
        
    
    con=l+datos
    resultados.append(con)
    imprimir(resultados)
        
def imprimir(l):
    for n in range(len(l)):
        print(l[n])

    
m=[]
def main():
    print("***PROGRAMA BREAKER***")
    print("Adivina el numero de 4 díjitos: [----]")
    print("Indicaciones:")
    print("Ningún numero se repite")
    print("Sí hay un numero parecido pero en la posición incorrecta se indicara con -")
    print("Sí hay un numero parecido y en la posición correcta se indicará con un *")
    print("Para salir presiona 'a' o escribe quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'a':
            return
        l=Leer
        if len(l)==4:
            d=usuario(l)
            if d:
                compara(d)
        else:print("tiene que ser 4 dijitos")
            
        
        
        
if __name__ == "__main__":
	main()
