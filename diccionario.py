#!/bin/env/python
import caracteres
from caracteres import Valores
mary=Valores()
class Diccion:
    mayuscula=mary.mayuscula()
    minuscula=mary.minuscula()
    numeros=mary.numeros()
    signos=mary.signos()
    espacio=mary.espacio()
    malong=len(mayuscula)-1
    minlong=len(minuscula)-1
    numlong=len(numeros)-1
    siglong=len(signos)-1
    esplong=len(espacio)-1

    def diccionario(self,var):
        #variable xela es el diccionario que va a contener los caracteres
        mayuscula=self.mayuscula
        minuscula=self.minuscula
        numeros=self.numeros
        signos=self.signos
        espacio=self.espacio
        cont=0
        xela={mayuscula[0]:'loa',mayuscula[1]:'kia',mayuscula[2]:'gsr',
              mayuscula[3]:'aol',mayuscula[4]:'3rt',mayuscula[5]:'3bt',
              mayuscula[6]:'st7',mayuscula[7]:'i9o',mayuscula[8]:'1ko',
              mayuscula[9]:'mj6',mayuscula[10]:'pq3',mayuscula[11]:'kw0',
              mayuscula[12]:'vip',mayuscula[13]:'9jo',mayuscula[14]:'wg5',
              mayuscula[15]:'f5a',mayuscula[16]:'s4n',mayuscula[17]:'t9c',
              mayuscula[18]:'h1a',mayuscula[19]:'00y',mayuscula[20]:'ed7',
              mayuscula[21]:'t7j',mayuscula[22]:'kw8',mayuscula[23]:'r2f',
              mayuscula[24]:'i6g',mayuscula[25]:'ro5',
              minuscula[0]:'S9K',minuscula[1]:'M3N',minuscula[2]:'Q9K',
              minuscula[3]:'D8I',minuscula[4]:'9ML',minuscula[5]:'K2V',
              minuscula[6]:'R9K',minuscula[7]:'N1X',minuscula[8]:'XS6',
              minuscula[9]:'5GF',minuscula[10]:'L1X',minuscula[11]:'W0Z',
              minuscula[12]:'NG7',minuscula[13]:'ST7',minuscula[14]:'P4D',
              minuscula[15]:'H80',minuscula[16]:'EV1',minuscula[17]:'K8C',
              minuscula[18]:'T58',minuscula[19]:'Y52',minuscula[20]:'RHL',
              minuscula[21]:'UW0',minuscula[22]:'SJ3',minuscula[23]:'K59',
              minuscula[24]:'BY7',minuscula[25]:'D3D',
              numeros[0]:'2D5',numeros[1]:'qS9',numeros[2]:'Tg7',numeros[3]:'Gs7',numeros[4]:'5G0',numeros[5]:'F31',numeros[6]:'T00',numeros[7]:'S5Q',
              numeros[8]:'C4f',numeros[9]:'8H7',

              signos[0]:'09D',signos[1]:'66Y',signos[2]:'98O',signos[3]:'43E',
              signos[4]:'56F',signos[5]:'01H',signos[6]:'63K',signos[7]:'11W',
              signos[8]:'03S',signos[9]:'44V',signos[10]:'A8O',signos[11]:'99N',
              signos[12]:'30D',signos[13]:'88J',signos[14]:'11M',signos[15]:'66S',
              signos[16]:'77G',signos[17]:'11A',signos[18]:'49L',signos[19]:'37G',
              signos[20]:'59O',signos[21]:'57U',signos[22]:'41D',signos[23]:'22C',
              signos[24]:'48F',signos[25]:'55T',signos[26]:'05X',signos[27]:'67E',
              signos[28]:'22B',signos[29]:'00I',signos[30]:'03A',signos[31]:'87H',

              espacio[0]:'Sa6',espacio[1]:'Wp0',espacio[2]:'Xq4',espacio[3]:'Yh1',
              espacio[4]:'Vs6',espacio[5]:'Ry7',' ':'   '


              }
        return xela.get(var)



    def diccionario2(self,var):
        mayuscula=self.mayuscula
        minuscula=self.minuscula
        numeros=self.numeros
        signos=self.signos
        espacio=self.espacio
        xela={'loa':mayuscula[0],'kia':mayuscula[1],'gsr':mayuscula[2],
              'aol':mayuscula[3],'3rt':mayuscula[4],'3bt':mayuscula[5],
              'st7':mayuscula[6],'i9o':mayuscula[7],'1ko':mayuscula[8],
              'mj6':mayuscula[9],'pq3':mayuscula[10],'kw0':mayuscula[11],
              'vip':mayuscula[12],'9jo':mayuscula[13],'wg5':mayuscula[14],
              'f5a':mayuscula[15],'s4n':mayuscula[16],'t9c':mayuscula[17],
              'h1a':mayuscula[18],'00y':mayuscula[19],'ed7':mayuscula[20],
              't7j':mayuscula[21],'kw8':mayuscula[22],'r2f':mayuscula[23],
              'i6g':mayuscula[24],'ro5':mayuscula[25],
              'S9K':minuscula[0],'M3N':minuscula[1],'Q9K':minuscula[2],
              'D8I':minuscula[3],'9ML':minuscula[4],'K2V':minuscula[5],
              'R9K':minuscula[6],'N1X':minuscula[7],'XS6':minuscula[8],
              '5GF':minuscula[9],'L1X':minuscula[10],'W0Z':minuscula[11],
              'NG7':minuscula[12],'ST7':minuscula[13],'P4D':minuscula[14],
              'H8O':minuscula[15],'EV1':minuscula[16],'K8C':minuscula[17],
              'T58':minuscula[18],'Y52':minuscula[19],'RHL':minuscula[20],
              'UW0':minuscula[21],'SJ3':minuscula[22],'K59':minuscula[23],
              'BY7':minuscula[24],'D3D':minuscula[25],
              '2D5':numeros[0],'qS9':numeros[1],'Tg7':numeros[2],'Gs7':numeros[3],'5G0':numeros[4],'F31':numeros[5],'T00':numeros[6],'S5Q':numeros[7],
              'C4f':numeros[8],'8H7':numeros[9],

              '09D':signos[0],'66Y':signos[1],'98O':signos[2],'43E':signos[3],
              '56F':signos[4],'01H':signos[5],'63H':signos[6],'11W':signos[7],
              '03S':signos[8],'44V':signos[9],'A8O':signos[10],'99N':signos[11],
              '30D':signos[12],'88J':signos[13],'11M':signos[14],'66S':signos[15],
              '77G':signos[16],'11A':signos[17],'49L':signos[18],'37G':signos[19],
              '59O':signos[20],'57U':signos[21],'41D':signos[22],'22C':signos[23],
              '48F':signos[24],'55T':signos[25],'05X':signos[26],'67E':signos[27],
              '22B':signos[28],'00I':signos[29],'03A':signos[30],'87H':signos[31],

              'Sa6':espacio[0],'WP0':espacio[1],'Xq4':espacio[2],'Yh1':espacio[3],
              'Vs6':espacio[4],'Ry7':espacio[5],'   ':' '
              }

        return xela.get(var)

            

    

