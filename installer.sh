set -e
pkg install -y python
pkg install -y ffmpeg
pip install --upgrade pip
pip install --upgrade setuptools
pip install youtube-dl
echo "clear" >> ../usr/etc/bash.bashrc
echo "python /data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/musica.py" >> ../usr/etc/bash.bashrc
echo "exit" >> ../usr/etc/bash.bashrc
clear
echo "Instalación completa. Reinicia Termux."
kill -9 $PPID
