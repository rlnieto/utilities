# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
# Recorre el directorio en el que se ejecuta el script convirtiendo TODOS los
# ficheros que encuentra a unicode.
#
# Los ficheros convertidos se guardan en una carpeta llamada "salida" que se
# crea dentro de la carpeta actual. Si la carpeta de salida ya existe se
# sobreescriben los ficheros que ya existan con el mismo nombre
#----------------------------------------------------------------------------------
import os
import sys

DIRECTORIO_SALIDA = 'salida'  # nombre del directorio de salida
DIRECTORIO_ENTRADA = '.'   # directorio en el que se hará la búsqueda

#----------------------------------------------------------------------------------
# Crea el directorio de salida (de manera bastante rústica de momento...)
#----------------------------------------------------------------------------------
def crear_directorio_salida(nombreDirectorio):
    print('Creando directorio de salida...')
    try:
        os.stat(nombreDirectorio)
    except:
        os.mkdir(nombreDirectorio)


#----------------------------------------------------------------------------------
# Recorre los ficheros existentes en el directorio que llega como parámetro
# convirtiendo los caracteres utf8 a unicode escape
#----------------------------------------------------------------------------------
def procesar_directorio(carpeta_entrada, carpeta_salida):
    convertidos = 0

    for fichero in os.listdir(carpeta_entrada):
        rutaEntrada = os.path.join(carpeta_entrada, fichero)
        rutaSalida =  os.path.join(carpeta_entrada + '/' + carpeta_salida + '/', fichero)


        if os.path.isfile(rutaEntrada):
            print('Convirtiendo {0}'.format(rutaEntrada))

            # Abrimos ficheros
            infile = open(rutaEntrada, encoding="utf8")
            #outfile = open(rutaSalida, "w", encoding='unicode-escape')
            outfile = open(rutaSalida, "w", encoding='UTF-8')

            for linea in infile:
                #print(linea)
                linea = linea.encode('unicode-escape').decode('utf-8')

                # restauramos tabs y saltos de línea
                linea = linea.replace('\\n', '\n').replace('\\t', '\t')

                # restauramos acentos y ñ/Ñ
                linea = linea.replace('\\xe1', 'á').replace('\\xe9', 'é').replace('\\xed', 'í').replace('\\xf3', 'ó').replace('\\xfa', 'ú')
                linea = linea.replace('\\xc1', 'Á').replace('\\xc9', 'É').replace('\\xcd', 'Í').replace('\\xd3', 'Ó').replace('\\xda', 'Ú')
                linea = linea.replace('\\xf1', 'ñ').replace('\\xd1', 'Ñ')

                 # Caso especial: albanés. El carácter ë se sustituye érroneamente por \xeb y debería de ser \u00EB
                linea = linea.replace('\\xeb', '\\u00EB')

                outfile.write(linea)


            outfile.close()
            infile.close()
            convertidos = convertidos + 1
        else:
            print('Saltando directorio {0}'.format(rutaEntrada))

    print('\n\n{0} ficheros convertidos\n'.format(convertidos))


#----------------------------------------------------------------------------------
# Principal
#
#----------------------------------------------------------------------------------
crear_directorio_salida(DIRECTORIO_SALIDA)
procesar_directorio(DIRECTORIO_ENTRADA, DIRECTORIO_SALIDA)
