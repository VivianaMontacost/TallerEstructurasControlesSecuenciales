capital= float (input("Ingrese la cantidad de dinero a invertir: "))
interes = float (input ("Ingrese el porcentaje de interés que el banco pagará mensualmente:"))
ganancia=(capital*interes)
total= float(capital+ganancia)
print("En total de dinero al final de un mes será de: ", str(total))