#!/bin/env python
"""
Este script verifica que las correcciones por incompatibilidad con versiones downpipe anteriores se hayan aplicado. Si todo está correcto, lanza el programa.
"""

import os
from modulos.filemodify import inicio

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

#Instala termcolor
if not os.path.isfile(rabs + "correcciones/2"):
    if "termcolor" in os.popen("pip freeze").read():
        os.system("echo 'hecho' > " + rabs + "correcciones/2")
    else:
        instalar = os.system("pip install termcolor")
        if instalar == 0:
            os.system("echo 'hecho' > " + rabs + "correcciones/2")
            os.system("clear")
            print("Actualización completa.\nPresiona enter para abrir DownPipe.")
            os.system("read hola")

#Si todo está correcto, lanza el programa
nc = 2#Número de correcciones
if len([x for x in range(1, nc+1) if os.path.isfile(rabs + "correcciones/" + str(x))]) == nc:
    os.system("python " + rabs + "tracks-from-newpipe/downpipe.py")
