numero = int(input("Ingrese calidad del aire"))
if numero >= 0 and numero <= 99:
  print("Bueno")
elif numero >= 100 and numero <= 199:
  print("Regular")
elif numero >= 200 and numero <= 299:
  print("Alerta")
elif numero >= 300 and numero <= 499:
  print("Preemergencia")
else:
  print("Emergencia")





  cargo = input("¿cual es su cargo?")
  if cargo == "Ejecutivo":
    print("el sueldo Ejecutivo es 90")
  elif cargo == "Jefe":
    print("el sueldo de Jefe es 100")
  elif cargo == "Externo":
    print("el sueldo de Externo es 50")
  else:
    print("no existe")
