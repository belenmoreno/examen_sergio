def uno():
    len_cudrado = calcular_longitud()
    area = len_cudrado * len_cudrado #tambien se puede poner con ** pero sergio no quiere
    print(area)
    #return area

def calcular_longitud():
    longitud = int(input("cual es la longitud del lado del cuadrado: "))
    return longitud

def dos():
    base = float(input("introduce la base del triangulo "))
    altura = float(input("introduce la altura del cuadrado "))
    operacion = (base * altura)/2
    print(operacion)


def main():
    while 1:
        opcion = input("que opcion prefieres: calcular el area del cuadrado(1), calcular el area de un triangulo(2), salir del programa(3) ")
        if opcion == '1': 
           uno()
            # resultado = uno()
            #print (resultado)
        elif opcion == '2':
            dos()
        elif opcion == '3':
            return







if __name__ == "__main__":
    main()


