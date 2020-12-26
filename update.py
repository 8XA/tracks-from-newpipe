#!/bin/env python

import os, time

def update():
    os.system("clear")
    print("Verificando actualizaciones de script...")
    remoto = os.popen('cd tracks-from-newpipe && git fetch origin master && git checkout remotes/origin/master').read()
    local = os.popen('cd tracks-from-newpipe && git checkout master && git log --oneline').read()
    if "Your branch is behind" in local[:50]:
        print("Actualizando script...\n")
        os.system('rm -rf update')
        clonar = os.system('git clone https://github.com/8XA/tracks-from-newpipe.git update')
        if clonar == 0:
            os.system('rm -rf tracks-from-newpipe')
            os.system('mv update tracks-from-newpipe')
            print("\nActualización completa.")
            return 1

    else:
        os.system("clear")
        print("Script ya actualizado. Nada para hacer...")
        time.sleep(1)
        os.system("clear")
        return 0
