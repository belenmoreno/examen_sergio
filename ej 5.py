#5) Se pretende hacer un programa que pregunte cuantos años tenga al usuario para ver si puede acceder al garito. Si éste responde menos de 18 años se le mostrará un mensaje diciendo que no puede entrar a la discoteca. Si tiene 18 o más años se le mostrará un mensaje de bienvenida.
#5.1) Hacer una 2ª versión del programa en la que si el usuario es mayor de edad se le hagan dos preguntas más. Si va a querer 1 copa por 8€ o 2x12€. Mostrar por pantalla el precio final: la oferta que haya seleccionado + 21% de IVA. 
#5.2) Preguntar al usuario si además va a querer guardarropa. El usuario podrá decir 'si' o 'no', si elige que no se mostrará por pantalla: 'okey'. Si el usuario dice que 'sí' se le dirá que es gratuito si previamente seleccionó la oferta de 2 copas, si solo elegió una copa habrá que decirle que tiene que pagar 1€.
def main():
    edad = int(input("¿cuantos años tienes? "))
    if edad < 18:
        print("lo siento no puedes entrar en la discoteca :( ")
    elif edad >= 18:
        print("bienvenido a nuestra discoteca :) ")
        una_copa = 8
        dos_copas = 12
        IVA = 21
        copa = input("¿vas a querer una copa por 8€(una) o 2x12€(dos)? ")
        copa = copa.upper()
        if copa != 'UNA' and copa != 'DOS':
            print("Error al introducir copa")
            return
        if copa == 'UNA':
            print("el precio es de una copa es de " + str(una_copa) + " pero con el IVA el precio final es " + str(una_copa + (una_copa * (IVA/100))))
        elif copa == 'DOS':
            print("el precio es de dos copas es de " + str(dos_copas) + " pero con el IVA el precio final es " + str(dos_copas + (dos_copas * (IVA/100))))

        guardarropa = input("¿vas a querer guardarropa? (si o no) ")
        guardarropa = guardarropa.upper()

        if guardarropa == 'NO':
            print("okey! gracias!! ")
        elif guardarropa == 'SI':
            cop = input("¿cual es la opcion de copas que has elegido (8 o 12)? ")
            cop = cop.upper()
            if cop == '8':
                print("tienes que pagar 1€ más")
            elif cop == '12':
                print("el ropero es gratuito para ti!! ")

if __name__ == "__main__":
    main()
