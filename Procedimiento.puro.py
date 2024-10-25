#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

__objeto = 3  #objeto y estado global
            #lo alcanza todo el codigo


def doblar (): 
    """procedimiento puro que doblar"""
    global __objeto 
    __objeto = __objeto * 2


if __name__ == "__main__":
    
    print (__objeto) # 3
    doblar () # procedimiento puro
    print(__objeto) # 6
 
    