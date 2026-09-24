def main():
 #programa: Este programa calcula el salario neto de un empleado después de aplicar impuestos y deducciones.
    salario = float (input("Ingresa tu salario bruto mensual: "))
    Porcentaje = 16
    deducciones = float (input("Ingresa el monto de deducciones adicionales: "))
    impuesto = salario * (Porcentaje / 100)
    Salario_neto = salario - impuesto - deducciones
    print(f"Tu salario neto es: ${Salario_neto:.2f}")
if __name__ == "__main__":
    main()