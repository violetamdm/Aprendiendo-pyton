#continuación de pruebapython libro de python
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[1])
print(spam[0:4])
print(spam[:])
print(spam[0:6])
print(spam[0:2])
print(len(spam))
del spam[2] #elimina un elemento de la lista
print(spam)

spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50], [7]] #array de arrays
print(spam2)
print(spam2[0])
print(spam2[-1])
print(spam2[1][0]) #del 0 al 4

for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = 'n' #input() (quitar la n)
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size, color, disposition, "gato: ", cat)
print(enumerate(cat))
a=0
b='fat'
# enumerate(cat)
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
     print('Index ' + str(index) + ' in supplies is: ' + item)
import random 
pets = ['Dog', 'Cat', 'Moose']
auxpets = pets.copy()
resulchoice = random.choice(pets)
random.shuffle(auxpets)
print('pets: '+ str(pets) + ', choice: ' + resulchoice + ', suffle: ' + str(auxpets))
print(pets.index('Cat'))
pets.append('fish')
print(pets)
pets.insert(2, 'you')
pets.insert(2, 'you')
pets.insert(2, 'you')
print(pets)
pets.remove('you')
print(pets)
pets.sort()
print(pets)

#anotaciones
def suma(a: 'parametro 1', b: 'parametro 2') -> 'retorno':
    return a + b

print(suma.__annotations__)
print(suma('j', 'p'))

# Salida:
# {'a': 'parametro 1',
#  'b': 'parametro 2',
#  'return': 'retorno'}

def filtrar_pares(salida: 'list' = []) -> 'list':
    return [i for i in salida if i%2 == 0]
print(filtrar_pares.__annotations__)
print(filtrar_pares([1, 2, 3, 4, 5, 6]))
# Salida: [2, 4, 6]
def suma(a : int, b: int) -> int:
    return a + b

print(suma('k','l')) # kl

#diccionarios
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} #sintax

#Ejemplo uso de diccionarios:
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
'''
while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break
       if name in birthdays:
             print(birthdays[name] + ' is the birthday of ' + name)
       else:
          print('I do not have birthday information for ' + name)
          print('What is their birthday?')
          bday = input()
          birthdays[name] = bday #birthdays[name] aquí el name es 
                                #el identificador de cada valor 
                                #(pairs key-value) 
          print('Birthday database updated.')
'''
print(birthdays)
print(list(birthdays))
birthdays['Violeta'] = 'May 11'
print(birthdays)
print(list(birthdays))
print(birthdays.values())
print('values:')
for i in birthdays.values():
    print(i)

print(birthdays.keys())
print('keys:')
for i in birthdays.keys():
     print(i)

print(birthdays.items())
print('items:')
for k in birthdays.items():
     print(k)

#manipular strings
print(" \\ Hello there!\nHow are you?\nI\'m doing...\t\"fine\".")
#salida:
'''
 \ Hello there!
How are you?
I'm doing...    "fine".
'''
print(r" \\ Hello there!\nHow are you?\nI\'m doing...\t\"fine\".")
#salida:
'''
 \\ Hello there!\nHow are you?\nI\'m doing...\t\"fine\".
'''
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print("Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob")

saludar='Hola genete, hola python'
print(saludar)
print(saludar[3] + '=¿a?')
print(saludar[5:] + '=¿genete, hola python?')

x='Hello' in 'Hello, World'
print(x)
#True
x='Hello' in 'Hello'
print(x)
#True
x='HELLO' in 'Hello, World'
print(x)
#False
x= '' in 'spam'
print(x)
#True
x='cats' not in 'cats and dogs'
print(x)
#False

name = 'Al'
age = 4000
x=f'My name is {name}. Next year I will be {age + 1}.'
print(x)
#'My name is Al. Next year I will be 4001.'
x='My name is {name}. Next year I will be {age + 1}.'
print(x)
# My name is {name}. Next year I will be {age + 1}.
#upper para letras mayúsculas y lower para letras minúsculas:
x='HOLA'
print(x)
x = x.lower()
print(x)
x= x.upper().lower()
print(x)
x=x.upper()
print(x)
print(x, 'lower? ', x.islower())
print(x, 'uper? ' , x.isupper())
#isalpha devuelve true si no hay espacios en blanco " "
#en una cadena de letras
print('isalpha:')
print('hola'.isalpha()) # True
print(''.isalpha()) # False
print('hola7'.isalpha()) # False
print('ho la'.isalpha()) # False
#isalnum devuelve true si no hay espacios en blanco " "
#en una cadena de letras y números
print('isalnum:')
print('hola'.isalnum()) # True
print(''.isalnum()) # False
print('hola7'.isalnum()) # True
print('ho l'.isalnum()) # False
#isdecimal devuelve true si tiene solo numeros 
print('isdecimal:')
print(''.isdecimal()) # False
print('hola7'.isdecimal()) # False
print('7,7'.isdecimal()) # False
print('77'.isdecimal()) # True
#isspace devuelve true si tiene espacios en blanco, tabulaciones 
# o saltos de línea (\n)
print('isspace:')
print(''.isspace()) # False
print('hola7'.isspace()) # False
print('\n'.isspace()) # True
print('                 \n'.isspace()) # True
#istitle Devuelve True si empieza con una letra mayúscula 
# y no hay ninguna letra mayúscula mas
print('istitle:')
print('H'.istitle()) # True
print('H '.istitle()) # True
print('H- '.istitle()) # True
print('Hola 7'.istitle()) # True
print('Hola Amigos'.istitle()) # True
print('Hola -Je'.istitle()) # True
print(''.istitle()) # False
print('HOLA'.istitle()) # False
print('hola'.istitle()) # False
#
print('endswith:')
print('hola'.endswith('a'))
print('hola'.endswith('u'))
print('startswith:')
print('hola'.startswith('h'))
print('hola'.startswith('p'))
#join junta cadenas de una lista y split las separa en lista 
print('join: ')
print(', '.join(['gatos', 'ratas', 'murciélagos']))
print(' '.join(['Mi', 'nombre', 'es' , 'Simon']))
print('split: ')
print('Mi nombre es Simón'.split())
print('Mi nombre es Simón'.split('ABC'))
print('Mi nombre es Simón'.split('m'))
texto = '''Querida Alice,
¿Cómo has estado? Estoy bien.
Hay un recipiente en el refrigerador
que tiene la etiqueta "Experimento con leche".

Por favor, no lo beba.
Atentamente,
Bob'''
print(texto.split('\n'))
print('Mi nombre es Simón'.partition(' '))
print('Mi nombre es Simón'.partition('m'))
print('Mi nombre es Simón'.partition('Simón'))
print('Mi nombre es Simón'.partition('l'))
before, sep, after = '¡Hola, mundo!'.partition(' ')
print(before, sep, after)
#
print('Hola'.rjust(10))
print('Hola'.ljust(10), 'e')
print('Hola'.center(10), 'e')
print('Hola'.rjust(10, '='))
print('Hola'.ljust(10, '='), 'e')
print('Hola'.center(20, '='))
#Picnic

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000} 
#diccionario de elementos picnic 
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# strip quita espacios en blanco

frase = '  Yo soy tu padre   '
print(frase.strip()) #quita blos blancos de los estremos
print(frase.lstrip()) #quita los blancos de la Izq
print(frase.rstrip()) #quita los blancos de la Dcha

#
print(ord('A'))
print(chr(40))

#Pyperclip utiliza el portapapeles
import pyperclip
pyperclip.copy('¡Hola, mundo!')
x = pyperclip.paste()
print(x)
#¡Hola, mundo!
'''
TEXT = {'de acuerdo': """Sí, estoy de acuerdo. Eso me parece bien.""",
        'ocupado': """Lo siento, ¿podemos hacerlo más tarde esta semana o la semana que viene?""",
        ' upsell': """¿Considerarías hacer de esto una donación mensual?"""}

import sys
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
'''
pyperclip.copy('frase copiada \n segunda\n')
text = pyperclip.paste()
print('texto: ' + text)
lines = text.split('\n')
print('texto 2 vez: ' + text)
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print('impress: ' + text)

#Para crear un archivo bat se abre un fichero de texto y se guarda conb el 
#formato "." (todo tipo de archivos) y se guarda con la extensión al final .BAT
#El archivo bat sirve para ejecutar el programa y tiene un pause
#para que no se cierre el términal tras su ejecución y así poder 
#mostrarla mas detalladamente.

#Capitulo 6
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} 
print(myCat)
myCat2 = myCat.copy() 
myCat['Violeta'] = 'May 11'
print(myCat2)
print(myCat)