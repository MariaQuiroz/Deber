#EJERCICIO 1
#Andrango Ariana y Quiroz Maria

class Calculadora():

     def __init__(self):

        self.numero1 = float(input("Ingresar el primer número: "))
        self.numero2 = float(input("Ingresar el segundo número: "))

     def imprimir(self):

        print("Los números ingresados son ",self.numero1," y ",self.numero2)

     def sumar(self):

        suma=self.numero1+self.numero2
        print("La suma de los dos números es: ",suma)

     def restar(self):

        resta=self.numero1-self.numero2
        print("La resta de los dos números es: ",resta)

     def multiplicar(self):

        multiplicacion=self.numero1*self.numero2
        print("La multiplicación de los dos números es: ",multiplicacion)

     def dividir(self):
        division=self.numero1/self.numero2
        print("La división de los dos números es: ",division)

micalculadora=Calculadora()
micalculadora.imprimir()
micalculadora.sumar()
micalculadora.restar()
micalculadora.multiplicar()
micalculadora.dividir()
