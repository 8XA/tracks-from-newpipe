set -e
termux-setup-storage
pkg install -y python
pkg install -y ffmpeg
pip install --upgrade pip
pip install --upgrade setuptools
pip install youtube-dl
cp tracks-from-newpipe/musica.py musica.py
chmod +x musica.py
echo "clear" >> ../usr/etc/bash.bashrc
echo "python musica.py" >> ../usr/etc/bash.bashrc
echo "exit" >> ../usr/etc/bash.bashrc
rm -rf tracks-from-newpipe
echo " "
echo "Instalación completa. Reinicia Termux."
