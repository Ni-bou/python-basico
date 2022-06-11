#exponencial del numero 64 con una base de "2"
def exponente(n):
 for i in range(1, n):
     if 2 ** i == n:
         return i
     elif 2 ** i> n:
             return i - 1

print(exponente(64))

def exponente(resultado):
 exponente1 = 2
 if exponente1 == 0:
    return 1
 else:
    while exponente1 > 1:
          resultado //= 2
          exponente1 =+ 1
    return exponente1
print(exponente(64))

def exponente(n):
  for i in range(n):
    if 2**i > n:
        i -= 1
        break
    return i
print(exponente(65))

#maximo comun divisor de los numero 10 y 15, siendo este el numero "5"
#def mcd(n1, n2):

 #for i in range(1,7):
  # i += 1
   #if n1 % i == 0 and n2 % i == 0:
    #return i
#print(mcd(87,31))

def mcd(n1,n2):
    maximo_comun_divisor = 0
    i = 1
    while i < n1:
        if n1 % i == 0 and n2 % i == 0:
            maximo_comun_divisor = i
        i += 1
    return maximo_comun_divisor
print(mcd(14,98))

def mcd(n1,n2):
    k = 0
    if n1 <= n2:
        k = n1
    else:
        k = n2
    while k > 1:
        if n1 % k ==0 and n2 % k == 0:
            break
        k = k - 1
    return k
print(mcd(10,15))

