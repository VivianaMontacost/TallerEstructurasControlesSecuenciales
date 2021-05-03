"""
entradas 
hombres int numerodehombres
mujeres int numerodemujeres
salidas
porcentajehombres float porcentajehombres
porcentajemujeres float porcentajehombres
"""
numerodehombres=int (input ("Ingrese el número de estudiantes hombres: "))
numerodemujeres=int (input ("Ingrese el número de estudiantes mujeres: "))
totalestudiantes=(numerodehombres+numerodemujeres)
porcentajemujeres=((numerodemujeres*100)/totalestudiantes)
porcentajehombres=((numerodehombres*100)/totalestudiantes)
print ("El porcentaje de mujeres en la clase es de:" +str(porcentajemujeres))
print ("El porcentaje de hombres en la clase es de:" +str(porcentajehombres))