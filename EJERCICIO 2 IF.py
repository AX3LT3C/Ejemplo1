num1=int(input("Ingrese un numero: "));
num2=int(input("Ingrese otro numero: "));
num3=int(input("Ingrese otro numero: "));
if(num1>num2):
    mensaje="El primer numero es el mayor";
elif(num2>num1):
    mensaje="El segundo numero es el mayor";
elif(num3>num2 and num1):
    mensaje="El tercer numero es el mayor";
else:
    mensaje="ERROR";
print(mensaje);