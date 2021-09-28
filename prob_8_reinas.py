#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:21:56 2019

@author: franciscohenriquez
"""

import numpy as np
import itertools

# Definiendo las funciones


def gen_reina (n_c):
    '''generando  la lista de reina
        se debe entregar el numero de columnas
    '''
    reina=list(range(1,n_c+1)

def eval_filas(n_c,com_r,c_reina):
    '''
    Se debe entregar el numero de columnas, las permutaciones de reinas (com_r)
    y el vector de columna (c_reina)
    '''
    filas_cumplen=[]
    for cr in com_r:
        fila_reina=list(cr)
        #esto genera los valores que se debe evaluar
        prueba_i=[]
        prueba_d=[]
        for i in range(n_c):
            prueba_i.append(c_reina[i]+fila_reina[i])
            prueba_d.append(c_reina[i]-fila_reina[i])
        # aca se realiza la evaluacion
        cumple=True
        nf=0
        while cumple and nf<=(n_c-1):
            for i in range(nf+1,n_c):
                if (prueba_i[nf]-prueba_i[i]==0) or (prueba_d[nf]-prueba_d[i]==0):
                    cumple=False
                    break
            nf+=1
        # se almacena si la combinacion cumple las condiciones
        if cumple:
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

filas_cumplen=busca_reinas(8)






