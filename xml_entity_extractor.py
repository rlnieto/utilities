#!/usr/bin/python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# Lee un fichero XML y lo divide en N ficheros usando como delimitador
# el tag introducido como parámetro y su cierre
#
# Los ficheros de salida tendrán nombres correlativos (fichero_salida0.txt,
# fichero_salida1.txt...)
#------------------------------------------------------------------------------
import sys

MENSAJE_AYUDA = '\nDivide un fichero XML en sus entidades. Uso: {0} fichero_entrada tag_delimitador\n\n'.format(sys.argv[0].split('.')[0])

# Entrada: fichero a descomponer y tag a utilizar. Genera tantos ficheros como
# entidades empicen y terminen con ese tag
if len(sys.argv) != 3:
    print (MENSAJE_AYUDA)
    sys.exit(1)

FICHERO_ENTRADA = sys.argv[1]
TAG_INICIAL = '<' + sys.argv[2] + '>'
TAG_FINAL = '</' + sys.argv[2] + '>'

guardar = False
ficheros_creados = 0

# Leemos el fichero línea a línea
infile = open(FICHERO_ENTRADA, "r")
contenido_fichero = []

for linea in infile:
    if TAG_INICIAL in linea:
        guardar = True

    if TAG_FINAL in linea:
        guardar = False

        # guardamos la última línea
        contenido_fichero.append(linea)

        # y salvamos todo a un fichero
        fichero_salida = open('fichero_salida{0}.txt'.format(ficheros_creados), 'w')
        for linea in contenido_fichero:
            fichero_salida.write(linea)
        fichero_salida.close()
        ficheros_creados += 1

        contenido_fichero = []


    if guardar:
        contenido_fichero.append(linea)
        #print(linea)

print(contenido_fichero)

infile.close()
