#!/bin/env/python
from string import ascii_letters, digits, hexdigits, punctuation, whitespace


class Valores:
    
    def minuscula(self):
        minuscula=ascii_letters[:26]
        return minuscula

    def mayuscula(self):
        mayuscula=ascii_letters[26:]
        return mayuscula

    def numeros(self):
        numeros=digits
        return numeros

    def signos(self):
        signos=punctuation
        return signos

    def espacio(self):
        espacios=whitespace
        return espacios



