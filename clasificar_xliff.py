# -*- coding: utf-8 -*-

import os
import sys
import shutil
import argparse
from stat import *
from pathlib import Path

'''
    Copia todos los fuentes jpli de una aplicación desde la ruta en la que estén
    sin importar los niveles de subcarpetas que haya

'''


companies = ['linguaserve', 'codex', 'transerve']


'''
    Recorre el árbol de directorios recursivamente llamando a una función
    de callback cada vez que encuentra un fichero

'''
def walktree(root, callback):

   for fichero in os.listdir(root):
       rutaCompleta = os.path.join(root, fichero)
       mode = os.stat(rutaCompleta)[ST_MODE]   # para saber el tipo de fichero

       # Directorio
       if S_ISDIR(mode):
           walktree(rutaCompleta, callback)
       # Fichero
       elif S_ISREG(mode):
           callback(rutaCompleta, fichero, root)
       # Cualquier otro...
       else:
           print('Tipo de fichero desconocido: %s' % rutaCompleta)


'''
    Callback para tratar los ficheros

'''
def buscar_proveedor(file):
    linguaserve = ['ar', 'ca', 'cs', 'hr', 'it']
    global_link = ['en-US', 'et']
    codex = ['pt', 'sk', 'sl', 'th']

    partes_fichero = file.split('.')

    if partes_fichero[0] in linguaserve:
        return 'linguaserve'

    if partes_fichero[0] in global_link:
        return 'global_link'

    if partes_fichero[0] in codex:
        return 'codex'

    #print(file)

    return 'desconocido'

def copiar_fichero(fullname, file, path):

    if file.find('.xliff') > 0:
        #print(fullname)
        proveedor = buscar_proveedor(file)

        #path_destino = Path('./' + proveedor + '/' + path[2:])
        #path_destino.mkdir(parents=True)

        path_destino = './' + proveedor + '/' + path[2:]
        os.makedirs(path_destino, exist_ok=True)
        shutil.copy(fullname, path_destino)

        print('Fichero {0} -> proveedor {1}'.format(path_destino, proveedor))


#-------------------------------------------------------------------------------------
#    main
#
#
#
#
#-------------------------------------------------------------------------------------
if __name__ == '__main__':

    walktree('.', copiar_fichero)
