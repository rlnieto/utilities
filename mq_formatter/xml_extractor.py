#!/usr/bin/python
# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------
# Lee un fichero XML de texto y extrae las líneas que incluyen tags XML y guarda
# el resultado en un fichero de texto con el mismo nombre y el sufijo
# '_formateado'
#------------------------------------------------------------------------------
import sys
import re
import os.path as path

#---------------------------------------------------------------------------------
#  extraer_xml
#
#  Entrada: nombre del fichero de entrada
#  Salida: lista con las líneas del fichero que tienen tags XML
#---------------------------------------------------------------------------------
def extraer_xml(fichero_entrada):
    # Comprobamos que el fichero exista
    if not path.exists(fichero_entrada):
        print('No se encuentra el fichero de entrada: {0}\n'.format(fichero_entrada))
        sys.exit(1)

    # El fichero existe => lo formateamos en varias líneas
    MENSAJE_AYUDA = '\nFormatea un fichero XML generado por SIMPA en varias líneas. Uso: {0} fichero_entrada\n\n'.format(sys.argv[0].split('.')[0])
    PATRON_TAG_XML = '([\t]*)(<.[^(><.)]+>)'   # tag de apertura seguido de cualquier cosa que no sea un tag de cierre y apertura de un nuevo tag

    patron = re.compile(PATRON_TAG_XML)
    datos_salida = []


    # Leemos el fichero
    infile = open(FICHERO_ENTRADA, "r")
    contenido_fichero = infile.read().split('\\n')   # es sólo una línea

    for linea in contenido_fichero:
        linea_formateada = linea.replace('\\t', '\t').replace('\\"', '"')

        # Pintamos la línea si tiene un tag XML. TODO: econtrar un método más eficiente??
        tags = patron.match(linea_formateada)
        if tags:
            datos_salida.append(linea_formateada)

    infile.close()

    return datos_salida

#---------------------------------------------------------------------------------
#  lista_a_fichero
#
#  Crea un fichero con el contenido de una lista (una línea por item de la lista)
#
#  Entrada: lista, nombre del fichero de salida
#  Salida: ninguna
#
#  OJO: si el fichero de salida existe, LO SOBREESCRIBE
#---------------------------------------------------------------------------------
def lista_a_fichero(lista, fichero_salida):
    fout = open(fichero_salida, "w")

    for linea in datos_salida:
        fout.write(linea + '\n')

    fout.close()


#---------------------------------------------------------------------------------
#  main
#  ----
#  Entrada: fichero a formatear. Genera un fichero con una línea por tag XML
#
#
#
#---------------------------------------------------------------------------------
if len(sys.argv) != 2:
    print (MENSAJE_AYUDA)
    sys.exit(1)

FICHERO_ENTRADA = sys.argv[1]
datos_salida = extraer_xml(FICHERO_ENTRADA)

# Grabamos el XML en un fichero
fichero_salida = FICHERO_ENTRADA + '_formateado.xml'
lista_a_fichero(datos_salida, fichero_salida)

print('\nProceso finalizado! (datos de salida en: {0})\n'.format(fichero_salida))
