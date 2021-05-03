h=float (input("Ingrese el número de horas trabajadas:"))
preciohora=50000
salariobruto= (h*30000)
impuestos= (salariobruto*0.20)
salarioneto=(salariobruto-impuestos)
print("El salario neto es de:", str(salarioneto))