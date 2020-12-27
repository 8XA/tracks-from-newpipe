#!/bin/env python
import os, curses, sqlite3, string, sys
from update import update


#FUNCIÓN SALIR
def salir():
    i = input("\nPresiona enter para salir.")
    sys.exit()


#FORMATOS
formatos = ("mp3","m4a")
if not os.path.isfile("settings/settings"):
    os.system("echo 0 > settings/settings")


#VERIFICANDO ACTUALIZACIONES DEL SCRIPT
lista_ac = ("siac","noac") #Actualizar, o no actualizar
if not os.path.isfile('settings/actualizar'):
    os.system('mkdir settings && echo "<-\n " > settings/actualizar')
with open("settings/actualizar") as ac:
    selec_actualizacion = ac.readlines()
if selec_actualizacion[0][:-1] == "<-": 
    if update() == 1:
        i = input("Debes reiniciar Termux.\nPresiona Enter para salir.")
        sys.exit()


#DETERMINANDO EL NÚMERO DE CARACTERES POR LÍNEA
screen = curses.initscr() 
num_cols = screen.getmaxyx()[1]
curses.endwin()
os.system("stty sane && clear")


#DEFINE LO QUE VA A IMPRIMIRSE ANTES DE INGRESAR OPCIONES
def pantalla():
    global db_existe, num_codec, local_playlists, youtube_playlists, conexion, cursor, num_cols
    os.system("clear")


    #IMPRIMIENDO TÍTULO
    print(num_cols*"=")
    titulo = "<- DOWNPIPE ->"
    subtitulo = "Yet another youtube track downloader"
    print(((num_cols-len(titulo))//2)*" " + titulo)
    print(((num_cols-len(subtitulo))//2)*" " + subtitulo)
    print(num_cols*"=")


    #EXPLORACIÓN E IMPRESIÓN DE LISTAS DE LA BASE DE DATOS
    db = "storage/downloads/newpipe.db"
    try:
        #Abriendo la base de datos
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()

        #Nombres e identificadores de listas locales
        cursor.execute('SELECT * from playlists')
        local_playlists = cursor.fetchall()

        #Nombres y URLs de listas de youtube
        cursor.execute('SELECT * from remote_playlists')
        youtube_playlists = cursor.fetchall()

        #Imprime listas locales
        if len(local_playlists) > 0:
            print("\nLISTAS LOCALES")
            for x in range(len(local_playlists)):
                print(x+1, local_playlists[x][1][:num_cols-(len(str(x+1))+1)])
            print()
        
        #Imprime listas de youtube
        if len(youtube_playlists) > 0:
            print("LISTAS YOUTUBE")
            for x in range(len(youtube_playlists)):
                print(x+1+len(local_playlists), youtube_playlists[x][2][:num_cols-(len(str(x+1+len(local_playlists)))+1)])
            print()
        
        print(num_cols*"=")
        db_existe = True

    except:
        db_existe = False


    #IMPRIME CONFIGURACIONES
    try:
        with open("settings/settings") as f:
            num_codec = int(f.readlines()[0])
        with open("settings/actualizar") as ac:
            selec_actualizacion = ac.readlines()
    except:
        os.system("clear")
        print("Configuración inicial hecha. Vuelva a iniciar Termux.")
        salir()
    print("FORMATOS\tSCRIPT UPDATES")
    for x in range(len(formatos)):
        if x <= 1:
            actualizacion = lista_ac[x]
            selec_ac = selec_actualizacion[x]
        else:
            actualizacion, selec_ac = "",""

        if formatos[num_codec] == formatos[x]:
            selec_form = "<-"
        else:
            selec_form = ""
        print(formatos[x],selec_form,"\t\t" + actualizacion, selec_ac[:-1])
    print(num_cols*"=")


#INICIA IMPRESIÓN DE PANTALLA
pantalla()


#SELECCIÓN DE TAREA A EJECUTAR
try:
        
    link = "siac" #Es solo para inicializar la variable
    while link in lista_ac or link in formatos:
        if db_existe:
            print("Para descargar una lista de NewPipe, solo ingrese el número que le corresponde. De lo contrario solo ingrese una URL.")
            print(num_cols*"=")
        link = input("\nLista/canción a descargar ('s' para salir): ")
        if link.upper() == "S":
            salir()
        #Si es un cambio de formato
        elif link.lower() in formatos:
            os.system("echo " + str(formatos.index(link.lower())) + " > settings/settings")

        #Si es un cambio en la actualizacion
        elif link.lower() in lista_ac:
            if link.lower() == "siac":
                os.system('echo "<-\n " > settings/actualizar')
            else:
                os.system('echo " \n<-" > settings/actualizar')
        pantalla()

    carpeta = input("\nNombre de la carpeta ('s' para salir): ")
    if carpeta.upper() == "S":
        salir()
    elif carpeta == "":
        print(num_cols*"-" + "\n")
        i = input("Las pistas se guardarán directamente en tu carpeta de música debido a que no especificaste un nombre de carpeta. Deseas continuar (Sí: 's', No: solo Enter)? ")
        if i.upper != "S":
            salir()
    
    
    #VERIFICANDO QUE YOUTUBE-DL Y PIP ESTÉN ACTUALIZADOS
    os.system("clear")
    print("Verificando actualizaciones por cambios en la plataforma de youtube...\n\n")
    os.system('pip install --upgrade pip')
    os.system('pip install --upgrade youtube-dl')
    os.system("clear")
    
    
    #DEFINIENDO EL LINK DE DESCARGA
    #Devuelve valor booleano de si la variable "link" es un número
    is_number = len([d for d in link if d in string.digits]) == len(link)
    if is_number and db_existe:
        #Si es una lista local
        if int(link) <= len(local_playlists):
            #ID del playlist
            ID = local_playlists[int(link)-1][0]

            #Videos con el ID de playlist al que pertenecen y su posición en URLs
            cursor.execute('SELECT * from playlist_stream_join')
            IDs_totales = cursor.fetchall()

            #URLs con identificadores
            cursor.execute('SELECT * from streams')
            URLs = cursor.fetchall()

            #String de URLs a descargar
            link = "'" + "' '".join([enlace[2] for enlace in URLs if enlace[0] in [video[1] for video in IDs_totales if video[0] == ID]]) + "'"

        #Si es una lista de youtube
        elif int(link) <= len(youtube_playlists) + len(local_playlists):
            link = "'" + youtube_playlists[int(link)-len(local_playlists)-1][3] + "'"

    #Si es cualquier otra lista
    else:
        link = "'" + link + "'"


    #CERRANDO BASE DE DATOS
    if db_existe:
        conexion.close()


    #DESCARGANDO PISTAS
    print("Descargando música...\nPara cancelar la descarga: Ctrl+c\n\n" + num_cols*"=")
    os.system('youtube-dl --ignore-errors --extract-audio --audio-format ' + formatos[num_codec] + ' -o "storage/music/' + carpeta + '/%(title)s.%(ext)s" ' + link)
    print(num_cols*"=")
    salir()


except Exception as e:
    os.system("clear")
    print("\nVaya, algo salió mal...\n\n")
    print(num_cols*"-")
    print("\nEste fue el error:\n\n" + str(e) + "\n")
    print(num_cols*"-")
    salir()
