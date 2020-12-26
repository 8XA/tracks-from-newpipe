#!/bin/env python
import os, curses

#Determinando el número de caracteres por línea
screen = curses.initscr() 
num_cols = screen.getmaxyx()[1]
curses.endwin()
os.system("stty sane")


os.system("clear")
#while es solo para poder hacer break cuando lo requiera, no pretende hacer un bucle
while True:
    try:
        #Imprimiendo título
        print(num_cols*"=")
        titulo = "<- DOWNPIPE ->"
        subtitulo = "Yet another youtube track downloader"
        print(((num_cols-len(titulo))//2)*" " + titulo)
        print(((num_cols-len(subtitulo))//2)*" " + subtitulo)
        print(num_cols*"=")
        print()
        link = input("Lista/canción a descargar ('s' para salir): ")
        if link.upper() == "S":
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
        
        
        #Descargando pistas
        print("Descargando música...\n\n")
        r = os.system('youtube-dl --ignore-errors --extract-audio --audio-format mp3 -o "storage/music/' + carpeta + '/%(title)s.%(ext)s" "' + link + '"')
        if r == 0:
            os.system("clear")
            print("Las pistas disponibles en la lista fueron descargadas. Revisa tu carpeta de música.")
        i = input("\n\nPresiona enter para salir.")
        break


    except Exception as e:
        os.system("clear")
        print("\nAlgo salió mal, probablemente la lista tenía problemas, como quiera házsela de pedo a Saúl...\n\n")
        print(num_cols*"-")
        print("\nEste fue el error:\n\n" + str(e) + "\n")
        print(num_cols*"-")
        i = input("\n\nPresiona enter para salir.")
        break
