# singleton
import asyncio
from threading import Lock
async def add(x, y):
    print("add")
    return x + y
async def funcasincrona():
    print("funciasincrona")
    var1= await add(3, 6)
    print('salio de var1 = ' + str(var1))
    var2=await add(9, 16)
    print('salio de var2 =', str(var2))
    await asyncio.sleep(4) #duerme 4 segs
    print("4 seg")
    print("resultados var  1 y 2: ", var1, "     ",  var2)

asyncio.run(funcasincrona())

class clase1(object):
    def __init__(self, id: int, nombre:str) -> None:
        self.id = id
        self.nombre = nombre
        # no se que es esto se crea x defectop en la funcion __int__:  pass
    def __str__(self) -> str:
        return "%s tiene el id %s" % (self.nombre, str(self.id))
    def __getattribute__(self, __name: str) -> Any:
        pass 
    # pass se utiliza para no tener que escribir código 
    # y que no se produzca un error
    def __setattr__(self, __name: str, __value: Any) -> None:
        #self.__value
        pass

#Las superclases instancian clases, ene ste caso 
# myClass es una clase creada con type que es una superclase:
myClass = type('myClass',(),{'a':True})#type es una metaclase
'''
myClass = type('myClass',(),{'a':True})
es esto:
class myClass(object):
    a = True
'''
new_class = type('myClass',(),{})
class_object = new_class()
