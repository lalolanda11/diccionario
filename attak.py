import cadena
import os
#ruta=os.getcwd()+'/texto'
def stone(ruta):
    archivo=os.listdir(ruta)
    os.chdir(ruta)
    long=len(archivo)-1
    n=0
    while True:
        with open(archivo[long],'r') as f:
            leer=f.read()
            encriptar=cadena.encrypt(leer)
            f.close()
            with open(archivo[long],'w') as s:
                s.write(encriptar)
                s.flush()
        long=long-1
        if long < n:
            break


def xela(ruta):
    archivo=os.listdir(ruta)
    os.chdir(ruta)
    long=len(archivo)-1
    n=0
    while True:
        with open(archivo[long],'r') as f:
            leer=f.read()
            desencriptar=cadena.decrypt(leer)
            f.close()
            with open(archivo[long],'w') as s:
                s.write(desencriptar)
                s.flush()
        long=long-1
        if long < n:
            break


if __name__=='__main__':
    ruta=input('ruta : ')
    print('[e] encrypt [d] decrypt')
    opc=input(' opcio ')
    if opc == 'e':
        stone(ruta)
    elif opc == 'd':
        xela(ruta)





