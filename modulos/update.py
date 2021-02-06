#!/bin/env python

import os, time

def update(num_cols):
    rabs = '/data/data/com.termux/files/usr/share/downpipe/tracks-from-newpipe/'
    rama = 'master'
    os.system("clear")
    print("Verificando actualizaciones de script...\n")
    remoto = os.popen('cd '+ rabs + ' && git fetch origin ' + rama + ' && git checkout remotes/origin/' + rama).read()
    local = os.popen('cd ' + rabs + ' && git checkout ' + rama).read()
    if "commit" in local:
        print("Actualizando script...\n")
        os.system('rm -rf update')
        clonar = os.system('git clone --branch ' + rama + ' --single-branch https://github.com/8XA/tracks-from-newpipe.git update')
        if clonar == 0:
            os.system('rm -rf ' + rabs[:-1])
            os.system('mv update ' + rabs[:-1] + ' && clear')
            print(((num_cols-22)//2)*" " + "ACTUALIZACIÓN COMPLETA")
            print(num_cols*"=")
            with open(rabs + "/novedades","r") as nov:
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
