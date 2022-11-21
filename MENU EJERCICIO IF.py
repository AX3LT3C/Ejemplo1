opcion = '0'
while not (opcion == '6'):
    print(' 1. opcion 01')
    print(' 2. opcion 02')
    print(' 3. opcion 03')
    print(' 4. opcion 04')
    print(' 5. opcion 05')
    print(' 6. Salir')

    opcion = input('  --- ¿Opcion?: ')

    if (opcion == '1'):
        print(' **** menu opcion 01 ****')

        num1 = int(input("Ingrese un numero: "));
        num2 = int(input("Ingrese otro numero: "));
        if (num1 > num2):
            mensaje = "El primer numero es el mayor";
        elif (num2 > num1):
            mensaje = "El segundo numero es el mayor";
        else:
            mensaje = "Error";
        print(mensaje);

    elif (opcion == '2'):
        print(' **** menu opcion 02 ****')

        num1 = int(input("Ingrese un numero: "));
        num2 = int(input("Ingrese otro numero: "));
        num3 = int(input("Ingrese otro numero: "));
        if(num1>num2):
            if (num1 > num3):
                 mensaje=("El numero mayor es:",num1);
        elif (num2 > num1):
              if(num2>num3):
                 mensaje=("El numero mayor es:",num2);
        else:
            mensaje=("El numero mayor es:",num3);
print("El numero mayor es: ",mensaje);

    elif (opcion == '3'):
        print(' **** menu opcion 03 ****')

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

    elif (opcion == '4'):
        print(' **** menu opcion 04 ****')



    elif (opcion == '5'):
        print(' **** menu opcion 05 ****')



    elif (opcion == '6'):
        print(' **** Saliendo del menu  ****')


    else:
        print('No existe la opcion')