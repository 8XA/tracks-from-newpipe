#!/bin/env python
"""Este módulo modifica los archivos de configuración:
1.- Recupera el contenido del archivo
2.- Edita lo necesario
3.- Guarda la edición
"""

import os

bashrc = '/data/data/com.termux/files/usr/etc/bash.bashrc'
log = '/data/data/com.termux/files/usr/share/downpipe/log'

#Agregar renglon a bashrc
def agregar(renglon):
    global bashrc
    with open(bashrc[:-7] + 'tmp', "a") as file:
        file.write(renglon + "\n")


#Esta función intercambia los modos de inicio automático o inicio por comando
#aut
#com
#lim <- opción adicional para limpiar el bashrc
def inicio(operacion, ancho):
    #Mensajes de advertencia
    os.system("clear")
    if operacion.lower() == 'com':
        print(ancho * "=" + "\n" + ((ancho-10)//2)*" " + "IMPORTANTE:")
        print("=" * ancho + "\n")
        print("Acabas de seleccionar 'Inicio por comando'. Con esta opción, deberás ingresar el comando:")
        print('\n' + " " * ((ancho - 8)//2) + "'dp'\n")
        print("en el siguiente inicio de Termux si quieres ejecutar el script.\n")
        print("=" * ancho + "\n")
        i = input("Deseas confirmar esta operación (Sí: s | No: Enter)?: ")
        if i.lower() != 's':
            return 1

    global bashrc
    #COMANDO2 Y AUTOMÁTICO2 SON LOS RENGLONES MÁS ACTUALES
    comando = "alias downpipe='python /data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/musica.py'"
    comando2 = "alias dp='exec python /data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/musica.py'"
    automatico_old = "python tracks-from-newpipe/musica.py"
    automatico = "python /data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/musica.py"
    automatico2 = "exec python /data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/musica.py"

    #Lineas a editar (agregar o eliminar, según el caso)
    customConfigs = [comando, comando2, automatico_old, "clear", automatico, automatico2, "exit"]
    
    #Lee el bashrc
    with open(bashrc, "r") as file:
        lineas = file.readlines()
    
    #Elimina algún posible temporal previo
    os.system('rm ' + bashrc[:-7] + 'tmp &> ' + log)
    
    #Depura el bashrc eliminando las configuraciones de downpipe y generando un temporal
    for renglon in [linea[:-1] for linea in lineas if linea[:-1] not in customConfigs]:
        agregar(renglon)
    
    if operacion.lower() == 'aut':
        #Agrega configuración de inicio automatico al bash temporal
        agregar(automatico2)

    #Agrega configuración de inicio por comando al bash temporal
    elif operacion.lower() == 'com':
        agregar(comando2)
    
    #Limpia los comandos que se hayan agregado
    elif operacion.lower() == 'lim':
        pass
 
    #Elimina temporal generado
    else:
        os.system('rm ' + bashrc[:-7] + 'tmp &>' + log)

    #Si el temporal no fue eliminado, entonces su configuración esta completa y pasa a sustituir a bashrc
    if os.path.isfile(bashrc[:-7] + 'tmp'):
        os.system('mv ' + bashrc[:-7] + 'tmp ' + bashrc + " &> " + log)

    #Si todo sale bien
    return 0
