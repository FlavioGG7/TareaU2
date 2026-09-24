def main ():
#Este programa calcula el índice de masa corporal (IMC) de una persona a partir de su peso y altura. El IMC es una medida que se utiliza para evaluar si una persona tiene un peso saludable en relación con su altura.
    peso = float (input ("Ingresa tu peso en kilogramos: "))
    altura = float (input ("Ingresa tu altura en metros: "))
    Imc = peso / (altura * altura)
    print (f"Tu índice de masa corporal es: {Imc:.2f}")
if __name__ == "__main__":
    main ()
