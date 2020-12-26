#!/bin/env python

import os, time

def update():
    os.system("clear")
    print("Verificando actualizaciones de script...")
    local = os.popen('cd tracks-from-newpipe && git checkout master && git log --oneline').read()
    remoto = os.popen('cd tracks-from-newpipe && git fetch origin master && git checkout remotes/origin/master && git log --oneline').read()
    os.system("clear")
    print("local:", local)
    print()
    print("remoto:",remoto)
    i = input("...")
    if local != remoto:
        print("Actualizando script...")
        os.system('rm -rf update')
        clonar = os.system('git clone https://github.com/8XA/tracks-from-newpipe.git update')
        if clonar == 0:
            os.system('rm -rf tracks-from-newpipe')
            os.system('mv update tracks-from-newpipe')
            print("Actualización completa.")
            return 1

    else:
        print("Nada para hacer...")
        time.sleep(1)
        os.system("clear")
        return 0
