#aqui se selecciona, las primeras dos letras de un string y las dos ultimas de otro strin, uniendolas, haciendo
#haciendo un nuevo strin.
def unirlos(familia,abrigarse):
 return("familia"[0:2] + ("abrigarse"[-2:(len("abrigarse"))]))
print("familia"[0:2] + ("abrigarse"[-2:(len("abrigarse"))]))

#en este ejercicio se mezcla un string intercalado agragandole otro string ej:
#string: "paz", string: "so" = "psoasozso"
s = "paz"
resultado2 = ""
i = 0
while i<len(s):
 resultado = (s[len(s)-(len(s)-i)]) + "so"
 resultado2 = resultado2 + resultado
 i += 1
print(resultado2)
#al dejar el print apregado a la primera linea, nos dara el resuntado final, solo un resultado
#pero si dejamos el print identado al i += 1, entonces nos dara las tres vueltas que da

 #ejercicio donde me cuenta los 1 y 0 de una cadena de numeros y luego los resta por cantidades
s = "111000010"
s1 = (s.count("1"))
s2 = (s.count("0"))
if s1 > s2:
 print(s1 - s2)
else:
 print(s2 - s1)

#aqui quiere que solo las palabras mayusculas de un string, cambien al signo peso
 def reemplazo(string):
  i = 0
  while i < len(string):
   if string[i].isupper():
    string = string.replace(string[i], '$')
   i += 1
  return string