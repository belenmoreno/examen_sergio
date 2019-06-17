import os
def opcion_1(marca, modelo):
    f_coches = open('coches.txt', 'r')
    for linea in f_coches:
        campos = linea.split(' ')
        if campos[0] == marca and campos[1] == modelo:
            print("linea: "+linea)
            print("campos: "+str(campos))
    f_coches.close()


def opcion_2(marca, modelo, puertas, velocidad):
    f_coches = open('coches.txt', 'a+')
    f_coches.write("\n")
    f_coches.write(marca + ' ' + modelo + ' ' + puertas + ' ' + velocidad)
    f_coches.close()

def opcion_3(marca, modelo):
    f_coches = open('coches.txt', 'r')
    marcas = []
    modelos = []
    color = []
    puertas = []
    velocidad = []
    encontrado = 0
    for linea in f_coches:
        campos = linea.split(' ')
        if marca != campos[0] and modelo != campos[1]:
            marcas.append(campos[0])
            modelos.append(campos[1])
            color.append(campos[2])
            puertas.append(campos[3])
            velocidad.append(campos[4])
        else:
            encontrado = 1


    f_coches.close()

    if encontrado == 0:
        print("No existe el coche a borrar")
        return
    os.remove('coches.txt')
    f2 = open('coches.txt', 'w')

    i = 0
    while i < len(marcas): #basta con buscar la longitud de cualquiera de las listas ya que todas tienen la misma longitud
        f2.write(marcas[i] + ' ' + modelos[i] + ' ' + color[i] + ' ' + puertas[i] + ' ' + velocidad[i])
        i += 1

    f2.close()



def main():
    f_coches = open('coches.txt', 'w')
    f_coches.write("toyota auris rojo 5_puertas 230_km_por_hora\nseat ibiza negro 3_puertas 185_km_por_hora\nmercedes_benz C gris 5_puertas 290_km_por_hora\nford focus azul 3_puertas 205_km_por_hora ")
    #print(f_coches)
    f_coches.close()

    while 1:
        usuario = input("que quieres hacer: ver los datos de algun coche(1), añadir más coches a la lista(2) o quieres borrar algun coche debido a su venta(3) o pulsa cualquier otra opcion para salir del programa")
        if usuario == '1':
            marca = input("introduce la marca del coche  que quieras ver ")
            modelo = input("introduce el modelo del coche que quieras ver ")

            opcion_1(marca, modelo)
        elif usuario == '2':
            marca = input("introduce la marca del coche que quieres añadir: ")
            modelo = input("introduce el modelo del coche que quieres añadir: ")
            puertas = input("cuantas puertas tiene 3 o 5_puertas: ")
            velocidad_max = input("introduce la velocidad máxima: ")
            opcion_2(marca, modelo, puertas, velocidad_max)

        elif usuario == '3':
        
            marca = input("introduce la marca del coche ")
            modelo = input("introduce el modelo del coche que quieres ")
            opcion_3(marca, modelo)
        else:
            print("ADIOS\tCHAO")
            return

if __name__ == "__main__":
    main()