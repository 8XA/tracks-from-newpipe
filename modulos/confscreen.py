#!/bin/env/python

"""
Este módulo recibe como primer parámetro, el ancho en columnas de la pantalla. Y
como segundo parámetro, una lista de columnas de configuración, donde cada columna 
es representada por otra lista que contiene la posicion del selector y el nombre
de los elementos que la componen.

"""


def confscreen(ancho, lista):
    grid_base = ancho * " "
    grid = [list(grid_base)]

    n_pipes = len(lista)-1
    longitud_columna = (ancho - n_pipes) // len(lista)
    lista_long_col = [longitud_columna for x in lista]
    remanentes = longitud_columna * len(lista)

    k = 0
    while remanentes < (ancho-n_pipes):
        lista_long_col[k], remanentes, k = lista_long_col[k] + 1, remanentes + 1, k + 1

    for columna in lista:
        pos = lista.index(columna)
        if pos == 0:
            avance = 0
        else:
            avance = sum(lista_long_col[0:pos]) + pos

        columna[1] = " " * ((lista_long_col[pos] - len(columna[1]))//2) + columna[1]
        for posicion in range(1,len(columna)):
            if posicion > len(grid):
                grid.append(list(grid_base))
            if posicion-1 == columna[0]:
                columna[posicion] += " <="
            for x in range(len(columna[posicion])):
                grid[posicion - 1][x + avance] = columna[posicion][x]
        
    grid.insert(1, list(ancho * "-"))
    for pipe in range(n_pipes):
        for renglon in grid:
            renglon[sum(lista_long_col[0:pipe+1]) + pipe] = '|'

    for x in grid:
        print("".join(x))
    print(ancho * "=")
    

