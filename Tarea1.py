Ref1 = int(input('ingrese la cantidad de productos comprados con la referencia "001":'))
Ref2 = int(input('ingrese la cantidad de productos comprados con la referencia "002":'))
Ref3 = int(input('ingrese la cantidad de productos comprados con la referencia "003":'))
Ref4 = int(input('ingrese la cantidad de productos comprados con la referencia "004":'))
if Ref1 >= 50:
  Desc = 30
elif Ref2 >= 50:
  Desc = 30
elif Ref3 >= 50:
  Desc = 30
elif Ref4 >= 50:
  Desc = 30
else:
  Desc = 0
print(f'el descuento es de {Desc}%')