from diccionario import Diccion


def encrypt(var):
    st=''
    xela=''
    num=0
    long=len(var)-1
    crypt=Diccion()
    while True:
        st=crypt.diccionario(var[long])+st
        #xela=st+xela
        long=long-1
        if long < num:
            break
    return st

def decrypt(var):
    st=''
    xela=''
    long=len(var)
    num=long-3
    dcrypt=Diccion()
    while True:
        st=str(dcrypt.diccionario2(var[num:long]))+st
        long=long-3
        num=long-3
        if long < 0:
            break
    return st

if __name__=='__main__':
    d=input('Dato ')
    x=encrypt(d)
    print(encrypt(d))
    print(decrypt(x))

