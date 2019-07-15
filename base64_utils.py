#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
#
#
#
#
#------------------------------------------------------------------------------
import base64
import sys


# Entrada: fichero a codificar
if len(sys.argv) != 3:
    print ("Uso: base64_utils [encode | decode] nombre_fichero")
    sys.exit(1)

OPERACION = sys.argv[1]
FICHERO_ENTRADA = sys.argv[2]
FICHERO_SALIDA = sys.argv[2] + "." + OPERACION

ENCODE = 'encode'
DECODE = 'decode'

def codificar_fichero():
    with open(FICHERO_ENTRADA, "rb") as file:
        encoded_string = base64.b64encode(file.read())
        fout = open(FICHERO_SALIDA, "wb")
        fout.write(encoded_string)
        fout.close()

        #print (encoded_string.decode())

def decodificar_fichero():
    with open(FICHERO_ENTRADA, "rb") as file:
        decoded_string = base64.b64decode(file.read())
        fout = open(FICHERO_SALIDA, "wb")
        fout.write(decoded_string)
        fout.close()

#------------------------------------------------------------------------------
# main
#
#
#------------------------------------------------------------------------------
if OPERACION == ENCODE:
    codificar_fichero()
elif OPERACION == DECODE:
    decodificar_fichero()
else:
    print ("Operación incorrecta: " + OPERACION)
