#!/bin/env python

import os
from modulos.filemodify import inicio

def corrector():
    ruta = '/data/data/com.termux/files/home/'
    rabs = ruta + "../usr/share/downpipe/"
    #Verifica que exista el directorio de correcciones
    if not os.path.isdir(rabs + "correcciones"):
        os.system("mkdir " + rabs + "correcciones")

    #Arregla los remanentes de la versión 1.02.3
    if not os.path.isfile(rabs + "correcciones/1"):
        #Condiciones
        a = os.path.isfile(ruta + "settings/actualizar")
        b = os.path.isfile(ruta + "settings/settings")
        c = os.path.isfile(ruta + "tracks-from-newpipe/musica.py")

        if not False in (a,b,c,):
            #Transfiriendo configuración
            with open(ruta + "settings/settings", "r") as f:
                lineas = f.readlines()
            os.system("echo " + lineas[0][:-1] + " > " + rabs + "settings/FORMATO")

            #Reinstalando script
            inicio("lim", 5) #No necesita el 5, la función pide el parámetro aunque para esta opción no lo usa
            os.system("git clone --branch master --single-branch https://github.com/8XA/tracks-from-newpipe.git " + rabs + "tracks-from-newpipe && chmod +x " + rabs + "tracks-from-newpipe/installer.sh && " + rabs + "tracks-from-newpipe/installer.sh")

        if os.path.isfile(rabs + "tracks-from-newpipe/musica.py"):
            os.system("echo 'hecho' > " + rabs + "correcciones/1")

            #Eliminando remanentes
            os.system('rm -rf ' + ruta + "settings")
            os.system('rm -rf ' + ruta + "tracks-from-newpipe")

