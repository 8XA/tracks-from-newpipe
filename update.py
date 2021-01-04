#!/bin/env python

import os, time

def update(num_cols):
    os.system("clear")
    print("Verificando actualizaciones de script...\n")
    remoto = os.popen('cd tracks-from-newpipe && git fetch origin master && git checkout remotes/origin/master').read()
    local = os.popen('cd tracks-from-newpipe && git checkout master').read()
    if "commit" in local:
        print("Actualizando script...\n")
        os.system('rm -rf update')
        clonar = os.system('git clone --branch master --single-branch https://github.com/8XA/tracks-from-newpipe.git update')
        if clonar == 0:
            os.system('rm -rf tracks-from-newpipe')
            os.system('mv update tracks-from-newpipe && clear')
            print(((num_cols-22)//2)*" " + "ACTUALIZACIÓN COMPLETA")
            print(num_cols*"=")
            with open("tracks-from-newpipe/novedades","r") as nov:
                novedades = nov.readlines()
            for line in novedades:
                print(line[:-1])
            print("\n" + num_cols*"=")
            return 1

    else:
        os.system("clear")
        print("Script ya actualizado. Nada para hacer...")
        time.sleep(1)
        os.system("clear")
        return 0
