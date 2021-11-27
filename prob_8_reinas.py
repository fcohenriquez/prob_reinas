#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:21:56 2019

@author: franciscohenriquez
"""

import numpy as np
import itertools


def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates
    esta prueba usa la propiedad de que el set no tiene elementos duplicados
    en este algoritmo se detiene la evaluacion cuando se encuentra algun elemento duplicado. Su complejidad es a lo sumo n*ln(n)
    '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

def gen_reina (n_c):
    '''generando  la lista de reina
        se debe entregar el numero de columnas
    '''
    return(range(1,n_c+1))

def eval_filas(n_c,com_r,c_reina):
    '''
    Se debe entregar el numero de columnas, las permutaciones de reinas (com_r)
    y el vector de columna (c_reina)
    '''
    filas_cumplen=[]
    for cr in com_r:
        '''
        lo que se evalua si existe alguna suma de fila y columna de una reina es igual a otra
        '''
        fila_reina=list(cr)
        #esto genera los valores que se debe evaluar
        prueba_i=np.add(np.array(c_reina), np.array(fila_reina))
        prueba_d=np.add(np.array(c_reina), -np.array(fila_reina))

        # aca se realiza la evaluacion y se almacena si la combinacion cumple las condiciones
        if not (checkIfDuplicates_2(prueba_i) or checkIfDuplicates_2(prueba_d)):
                filas_cumplen.append(fila_reina)
    
    if len(filas_cumplen)<=10:
        print("estas son las "+str(len(filas_cumplen)) +" filas que cumplen:")
        for i in filas_cumplen:
            print(i) 
    else:
        print("estas son las primeras 10 de de las "+str(len(filas_cumplen)) +" filas que cumplen:")
        for i in range(10):
            print(filas_cumplen[i]) 
    return(filas_cumplen)


def busca_reinas(n_c):
    '''
    esto reune los pasos para encontrar las filas que cumplen
    '''
    reina=gen_reina(n_c)
    #generando las distintas combinaciones de reinas
    comb_reina=list(itertools.permutations(reina, r=n_c))
    print("Se deben evaluar "+ str(len(comb_reina))+" permutaciones")
    resultado=eval_filas(n_c,comb_reina, reina)
    return(resultado)

filas_cumplen=busca_reinas(4)

'''
n_c=11
print(len(list(itertools.permutations(gen_reina(n_c), r=n_c))))
[4, 40, 92, 352, 724, 2680]

'''




