```
export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get -o Dpkg::Options::="--force-confdef" upgrade -q -y --force-yes && pkg install -y git && git clone https://github.com/8XA/tracks-from-newpipe.git && chmod +x tracks-from-newpipe/installer.sh && tracks-from-newpipe/installer.sh 
```