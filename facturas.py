# Solicitar los costos de los servicios básicos
electricidad = float(input("Ingresa el costo de la electricidad: $"))
if electricidad < 10:
    print("El costo de la electricidad no puede ser negativo.")
    exit()

agua = float(input("Ingresa el costo del agua: $"))   
gas = float(input("Ingresa el costo del gas: $"))

# Calcular el total de la factura
total_factura = electricidad + agua + gas 

# Mostrar el total de la factura
print(f"\nEl total de la factura es: ${total_factura:.2f}")