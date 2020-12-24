export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -o Dpkg::Options::="--force-confdef" upgrade -q -y --force-yes
pkg install -y python
pkg install -y ffmpeg
pip install --upgrade pip
pip install --upgrade setuptools
pip install youtube-dl
cp storage/downloads/musica.py musica.py
chmod +x musica.py
echo "clear" >> ../usr/etc/bash.bashrc
echo "python musica.py" >> ../usr/etc/bash.bashrc
echo "exit" >> ../usr/etc/bash.bashrc
rm storage/downloads/installer.sh
rm storage/downloads/musica.py
rm installer.sh
echo " "
echo "Instalación completa. Reinicia Termux."
