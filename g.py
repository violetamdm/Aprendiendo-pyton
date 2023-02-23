s = "kjhfgdjkgkdjfghgjkbdfkjh"
n = int(2)
lista  = []
ascendente = True
x=0
for i in range(0, n):
    lista.append([])



for i in range(0, len(s)):
    if (ascendente == True):
        lista[x].append(s[i])
        if x < n-1:
            print(x, int(n-1))
            x = x + 1
        else:
            
ascendente  = True
print(lista)
