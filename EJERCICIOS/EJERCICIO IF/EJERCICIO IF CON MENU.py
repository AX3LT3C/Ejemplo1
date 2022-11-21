def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('opcion 4', accion4),
        '5': ('opcion 5', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')

def accion1():
    print('*********** Has elegido la opción 1 ************')
    print('********** MAYOR Y MENOR *********')

    num1 = int(input("Ingrese un numero: "));
    num2 = int(input("Ingrese otro numero: "));

    if (num1 > num2):
           mensaje = "El primer numero es el mayor";
    elif (num2 > num1):
           mensaje = "El segundo numero es el mayor";
    else:
            mensaje = "Error";
    print(mensaje);

def accion2():
    print('*********** Has elegido la opción 2 **********')
    print('*********** VALOR MAYOR ***********')

    num1 = int(input("Ingrese un numero: "));
    num2 = int(input("Ingrese otro numero: "));
    num3 = int(input("Ingrese otro numero: "));
    if(num1>num2):
         if (num1 > num3):
                 print("El numero mayor es:",num1);
    elif (num2 > num1):
         if(num2>num3):
                 print("El numero mayor es:",num2);
    else:
          print("El numero mayor es:",num3);

def accion3():
    print('********** Has elegido la opción 3 *********')
    print('*********** SUMA **********+')

    num1 = int(input("Ingrese un numero: "));
    num2 = int(input("Ingrese otro numero: "));
    num3 = int(input("Ingrese otro numero: "));
    resultado = num1 + num2 + num3;
    print("El resultado es: ", resultado);
    if (resultado % 7 == 0):
           mensaje = "El resultado es multiplo de 7";
    else:
           mensaje = "El resultado no es multiplo de 7";
    print(mensaje);

def accion4():
    print('*********** Has elegido la opcion 4 ************')
    print('********** PROMEDIO ************')

    num1=int(input("Ingrese un numero: "));
    num2=int(input("Ingrese otro numero: "));
    num3=int(input("Ingrese otro numero: "));
    suma=num1+num2+num3;
    prom=suma/3;
    if(prom%2==0):
         mensaje="El numero es par";
    else:
        mensaje="El numero es impar";
    print(mensaje);

def accion5():
    print('********* Has elegido la opcion 5 ********')
    print('*********** EMPRESA TELEFONIA ************')

    nombre=str(input("Ingrese su nombre: "));
    time1=int(input("Ingrese los minutos consumidos nacionales: "));
    time2=int(input("Ingrese los minutos consumidos internacionales: "));
    sumatime=int(time1+time2);
    total=0;
    print("El resultado es: ",sumatime);
    if(sumatime<=25):
        print("Los primeros 25 minutos son gratis y por lo cual su llamada es gratis");
    elif(time1<=25):
        acu=time1-25;
        time2+=acu;
        total=time2*2.5;
    else:
        time1-=25;
        total=(time1*0.5)+(time2*2.5);
        print("El total a pagar Q",total);

def salir():
    print('******* Saliendo del sistema ******')
    print('******** ADIOS ********')


if __name__ == '__main__':
    menu_principal()