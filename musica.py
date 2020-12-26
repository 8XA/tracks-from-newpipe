#!/bin/env python
import os, curses, sqlite3, string


#Determinando el número de caracteres por línea
screen = curses.initscr() 
num_cols = screen.getmaxyx()[1]
curses.endwin()
os.system("stty sane && clear")


#Formatos
formatos = ("mp3","m4a")
if not os.path.isfile("formatos.txt"):
    os.system("echo 0 > formatos.txt")


#Imprimiendo título
print(num_cols*"=")
titulo = "<- DOWNPIPE ->"
subtitulo = "Yet another youtube track downloader"
print(((num_cols-len(titulo))//2)*" " + titulo)
print(((num_cols-len(subtitulo))//2)*" " + subtitulo)
print(num_cols*"=")


#Explora la base de datos de NewPipe
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
        print("LISTAS LOCALES")
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


#Imprime formatos
print("FORMATOS")
with open("formatos.txt") as f:
    num_formato = int(f.readlines()[0])
for elemento in formatos:
    if formatos[num_formato] == elemento:
        seleccion = "<-"
    else:
        seleccion = ""
    print(elemento,seleccion)
print(num_cols*"=")


#while es solo para poder hacer break cuando lo requiera, no pretende hacer un bucle
while True:
    #Selección de tarea a ejecutar
    try:
        if db_existe:
            print("Para descargar una lista de NewPipe, solo ingrese el número que le corresponde. De lo contrario solo ingrese una URL.")
        link = input("Lista/canción a descargar ('s' para salir): ")
        if link.upper() == "S":
            break
        #Si es un cambio de formato
        elif link.lower() in formatos:
            os.system("echo " + str(formatos.index(link.lower())) + " > formatos.txt")
            break

        carpeta = input("\nNombre de la carpeta ('s' para salir): ")
        if carpeta.upper() == "S":
            break
        elif carpeta == "":
            print(num_cols*"-" + "\n")
            i = input("Las pistas se guardarán directamente en tu carpeta de música debido a que no especificaste un nombre de carpeta. Deseas continuar (Sí: 's', No: solo Enter)? ")
            if i.upper != "S":
                break
        
        
        #Verificando que youtube-dl y pip estén actualizados
        os.system("clear")
        print("Verificando actualizaciones por modificaciones en youtube...\n\n")
        os.system('pip install --upgrade pip')
        os.system('pip install --upgrade youtube-dl')
        os.system("clear")
        
        
        #Definiendo el link de descarga
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


        #Cerrando base de datos
        if db_existe:
            conexion.close()


        #Descargando pistas
        print("Descargando música...\n\n")
        os.system('youtube-dl --ignore-errors --extract-audio --audio-format ' + formatos[num_formato] + ' -o "storage/music/' + carpeta + '/%(title)s.%(ext)s" ' + link)
        i = input("\n\nPresiona enter para salir.")
        break


    except Exception as e:
        os.system("clear")
        print("\nVaya, algo salió mal...\n\n")
        print(num_cols*"-")
        print("\nEste fue el error:\n\n" + str(e) + "\n")
        print(num_cols*"-")
        i = input("\n\nPresiona enter para salir.")
        break
