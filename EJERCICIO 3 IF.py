num1=int(input("Ingrese un numero: "));
num2=int(input("Ingrese otro numero: "));
num3=int(input("Ingrese otro numero: "));
resultado=num1+num2+num3;
print("El resultado es: ",resultado);
if(resultado%2==0):
   mensaje="El resultado es multiplo de 7";
else:
    mensaje="El resultado no es multiplo de 7";
print(mensaje);