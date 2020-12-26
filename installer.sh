set -e
termux-setup-storage
pkg install -y python
pkg install -y ffmpeg
pip install --upgrade pip
pip install --upgrade setuptools
pip install youtube-dl
echo "clear" >> ../usr/etc/bash.bashrc
echo "python tracks-from-newpipe/musica.py" >> ../usr/etc/bash.bashrc
echo "exit" >> ../usr/etc/bash.bashrc
echo " "
echo "Instalación completa. Reinicia Termux."
