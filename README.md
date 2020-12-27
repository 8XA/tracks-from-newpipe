# tracks-from-newpipe

This script will help you to download the playlist tracks from Youtube and NewPipe using youtube-dl. | Este script te ayudará a descargar las pistas de las listas de reproducción de Youtube y NewPipe, usando youtube-dl.

---

It was tested on an android device. | El proceso fue testeado en un dispositivo android.

- Install termux from the playstore. | Instala termux desde la playstore.

  *The termux installation must to be clean. You'll not be able to use termux after the process, but for using this script only. | La instalación de termux debe de ser limpia. No podrás usar termux después del proceso, excepto para este script.
- If you want to continue, execute the next command in termux. | Si quiere continuar, ejecute el siguiente comando en termux:

```export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get -o Dpkg::Options::="--force-confdef" upgrade -q -y --force-yes && pkg install -y git && git clone https://github.com/8XA/tracks-from-newpipe.git && chmod +x tracks-from-newpipe/installer.sh && tracks-from-newpipe/installer.sh```

- In the middle of the process, the script will ask you for storage permission. Accept it. | En medio del proceso, el script le pedirá permiso de almacenamiento. Acéptelo.
- When the process is done, restart termux. The script will start automatically, so you can use it. | Cuando el proceso finalice, reinicie termux. El script iniciará automaticamente, entonces puede usarlo.

- Si quiere visualizar las listas de NewPipe, debe exportar su base de datos:
    - Opciones
    - Ajustes
    - Contenido
    - Exportar base de datos
    - Aceptar
    - Del archivo exportado, extraer newpipe.db en la carpeta de descargas
    - Reiniciar Termux

- If you want to view the NewPipe lists, you have to export their database:
    - Options
    - Settings
    - Content
    - Export database
    - OK
    - You have to extract the newpipe.db from the exported file and put it in the Download folder
    - Restart Termux

So you can do these actions:
1.- Download a track or a track list putting the YouTube list URL or the track YouTube URL.
2.- Choose between download formats typing "mp3" or "m4a" (withouth quotation marks).
3.- Choose between update the script or not when a new github commit is available ("siac" or "noac" without quotation marks).
4.- Download a NewPipe track list typing the playlist number.

Entonces usted puede ejecutar las siguientes acciones:
1.- Descargar una pista o una lista de reproducción, poniendo la URL de la lista o de la pista.
2.- Elegir entre los formatos de audio escribiendo "mp3" o "m4a" (sin comillas) según corresponda.
3.- Elegir entre actualizar el script cuando haya un commit disponible, o no ("siac" o "noac", sin comillas).
4.- Descargar una lista de reproducción de NewPipe escribiendo el número de la lista de reproducción.
