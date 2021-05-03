valorhora= 20000
horastrabajadas=120
horasextra=10
valorhoraextra=((valorhora*0.25)+valorhora)
recibidoporhoraextra=(valorhoraextra*horasextra)
sueldobase=(valorhora*horastrabajadas)
print("El sueldo base del empleado es de:", str(sueldobase),"pesos.")
deducciones=(sueldobase*0.14)
Sueldomenosdeducciones=(sueldobase-deducciones)
print("El sueldo base menos las deducciones es de:", str(Sueldomenosdeducciones),"pesos.")
Actualizaciónacademica=250000
total1=(Sueldomenosdeducciones+Actualizaciónacademica)
print("Añadiendo la actualización académica de 250.000 pesos:", str(total1),"pesos.")
dinerohijos=(3*173000)
total2=(total1+dinerohijos)
print("Añadiendo subsidio para los 3 hijos:", str(total2), "pesos.")
bonohogar=180000
total3=(total2+bonohogar)
print("Añadiendo el bono Hogar", str(total3),"pesos.")
total4=(total3+recibidoporhoraextra)
print("Más las horas extra trabajadas el salario neto sería de:", str(total4), "pesos.")