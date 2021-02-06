set -e
pkg install -y python
pkg install -y ffmpeg
pip install --upgrade pip
pip install --upgrade setuptools
pip install termcolor
pip install youtube-dl
echo "clear" >> /data/data/com.termux/files/usr/etc/bash.bashrc
echo "exec python /data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/musica.py" >> /data/data/com.termux/files/usr/etc/bash.bashrc
clear
echo "Instalación completa. Reinicia Termux."
read listo
