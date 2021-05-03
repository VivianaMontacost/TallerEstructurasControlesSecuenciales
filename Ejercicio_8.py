a= float(input("Digite el valor del lado A:"))
b= float(input("Digite el valor del lado B:"))
c= float(input("Digite el valor del lado C:"))
s=((a+b+c)/2)
area= (s*(s-a)*(s-b)*(s-c))*1/2
print("El valor del área es de:", str(area))