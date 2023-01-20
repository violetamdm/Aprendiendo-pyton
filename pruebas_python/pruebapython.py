
name = ''
#"break" se usa para salir del bucle
while name != 'your name':
     break
     print('Please type your name.')
     name = input()

print('Thank you!')

print('My name is')
#este for hace el incremento de variable automatico
for i in range(5):
     print('Jimmy Five Times (' + str(i) + ')')

print('bucle con range de 0 a 5:')
for i in range(0, 5):
     print('Jimmy Five Times (' + str(i) + ')')
#desde el 12 hasta el 15
for i in range(12, 16):
     print(i)
#cuando tiene 3 parametros si el tercero es x salta de x numeros
for i in range(0, 10, 2):
     print(i) # 0 2 4 6 8
#bucle descendente
print('descendente de 5 a -1:')
for i in range(5, -1, -1):
     print(i)
print('probando random desde 1 hasta 10')
import random 
for i in range(5):
    print(random.randint(1, 10))
wins, losses, ties = ("j", "k", "i")
print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
import sys
#sys.exit() # Quit the program

#operadores:
print('2//1=' + str(2//1))
print('2/1=' + str(2/1))
print('2**3=' + str(2**3))
print('2+4j=' + str(2 + 4j))
print('este numero es de tipo:' + str(type(4j +2)))
#funciones
#el return no cambia
def hello(name):
     print('Hello, ' + name)
hello('Violeta')
print('cats', 'dogs', 'mice') #cats dogs mice
print('cats', 'dogs', 'mice', sep=',') #cats,dogs,mice
print('cats', 'dogs', 'mice', sep=', ') #cats, dogs, mice
eggs = 0
def spam():
     eggs = 31337
spam()
print(eggs)

def spam():
     eggs = 99
     bacon()
     print(eggs) 

def bacon():
     ham = 101 #no esta definida 
     eggs = 0

spam()

#esto da error
'''
def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()
'''
#print(eggs) se ejecuta antes de que se le asigne algo a egg
'''
def spam2(divideBy):
    return 42 / divideBy

print('spam2='+spam2(2))
print('spam2='+spam2(12))
print('spam2='+spam2(0))
print('spam2='+spam2(1))
'''
print('probando try except & finall (final es "esto acabo")')
#esto es como el try cach de java manejo de excepciones
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    else: #esto no lo entiendo muy bien es para cuando el bloque try se ejecuta sin errores
        print('no hay errores')
    finally:
        print('esto acabo')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#se para con control +  c
'''
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
    '''