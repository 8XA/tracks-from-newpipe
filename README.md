# tracks-from-newpipe

This script help you to download mp3 playlists from Youtube using youtube-dl. With a near future version you'll be able to download the local newpipe playlists too. | Este script te ayudará a descargar listas de reproducción en mp3 de Youtube, usando youtube-dl. En una próxima futura versión podrás descargar también las listas de reproducción locales de NewPipe.

---

It was tested on an android device. | El proceso fue testeado en un dispositivo android.

- Install termux from the playstore. | Instala termux desde la playstore.

  *The termux installation must to be clean. You'll not be able to use termux after the process, but for using this script only. | La instalación de termux debe de ser limpia. No podrás usar termux después del proceso, excepto para este script.
- If you want to continue, execute the next command in termux. | Si quiere continuar, ejecute el siguiente comando en termux:

```export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get -o Dpkg::Options::="--force-confdef" upgrade -q -y --force-yes && pkg install -y git && git clone https://github.com/8XA/tracks-from-newpipe.git && chmod +x tracks-from-newpipe/installer.sh && tracks-from-newpipe/installer.sh```

- In the middle of the process, the script will ask you for storage permission. Accept it. | En medio del proceso, el script le pedirá permiso de almacenamiento. Acéptelo.
- When the process is done, restart termux. The script will start automatically, so you can use it. | Cuando el proceso finalice, reinicie termux. El script iniciará automaticamente, entonces puede usarlo.
