# -*- coding: utf-8 -*-
"""
Created on Fri May 21 21:39:46 2021

@author: FCRX
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)         # Configura las gráficas.
plt.rc('font', size=9)       
plt.rc('axes', titlesize=9)
plt.rc('axes', labelsize=9)
plt.rc('xtick', labelsize=9)
plt.rc('ytick', labelsize=9)
plt.rc('legend', fontsize=9)
plt.rc('figure', titlesize=9)

infile = open("segundointento.txt", 'r')
l_tensiones = []
l_corrientes = []
for line in infile:
    x = line.split()
    l_corrientes.append(float(x[1]))
    l_tensiones.append(float(x[2]))
infile.close()

pendientes = []
error_pendientes = []

fila = 0

while fila < len(l_corrientes):
    
    z = np.polyfit(l_corrientes[fila:fila+21],l_tensiones[fila:fila+21],1, cov=True)
    
    pendientes.append(z[0][0])
    error_pendientes.append(np.sqrt(z[1][1][1]))
    
    fila += 22
    
plt.figure(figsize = (3.54, 2.9), dpi = 300)
plt.plot(list(range(1,len(pendientes)+1,1)), pendientes)    
#plt.xlim((0.5,5.0))
#plt.ylim((-0.04, 1.04))
plt.xlabel(r'\textrm{Número de pulso }$N$')
plt.ylabel(r'\textrm{Resistencia }($\Omega$)', labelpad = 8)
plt.grid()
plt.tight_layout(pad = 0.05)
plt.savefig("tet.png")
plt.show()
plt.close()