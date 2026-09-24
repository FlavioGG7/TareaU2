def main ():
#Este programa calcula el área de un rectángulo a partir de los valores de sus lados. El área se obtiene multiplicando la longitud del primer lado por la longitud del segundo lado.
    lado1 = float(input("Ingrese el valor del primer lado del rectángulo: "))
    lado2 = float(input("Ingrese el valor del segundo lado del rectángulo: ")) 
    area = lado1 * lado2
    print("El área del rectángulo es:", area)
if __name__ == "__main__":
    main()