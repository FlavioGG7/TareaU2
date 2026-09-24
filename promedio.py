def main ():
#Este programa caclcula el promedio a partir de 3 numeros que ingresa el usuario
    N1 = float(input("Ingresa el primer numero: "))
    N2 = float(input("Ingresa el segundo numero: "))
    N3 = float(input("Ingresa el tercer numero: "))
    N4 = (N1 + N2 + N3) / 3
    print(f"El promedio de los tres numeros es: {N4:.2f}")
if __name__ == "__main__":
    main()