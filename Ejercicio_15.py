valorproducto=float(input("Ingrese el valor total del producto:"))
valorpagado=float(input("Ingrese el valor pagado:"))
diferencia=(valorproducto-valorpagado)
porcentajedescuento=((diferencia*100)/valorproducto)
print("El descuento fue de:", str(porcentajedescuento), "%")