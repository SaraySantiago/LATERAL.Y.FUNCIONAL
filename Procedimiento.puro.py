#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

__objeto = [11, 22, 33]  #objeto y estado global
            #lo alcanza todo el codigo


def doblarLista (posicion): 
    """procedimiento puro que doblar un item de una lista particular __objeto, que es global"""
    global __objeto 
    __objeto[posicion] = __objeto[posicion] * 2
    
def doblar (lista, donde):
    pass  
# TO DO: que funcione!

if __name__ == "__main__":
    
    print (__objeto) # [11,22,33]
    doblarLista (1) # procedimiento puro
    print(__objeto) # [11,44,33]
 
    lista0= ["ma", "pa"]
 
    print (lista0) # [ma, pa]
    doblar (lista0, 1) # procedimiento puro
    print(lista0) # [ma, papa]
    