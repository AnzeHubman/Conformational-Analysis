#**********************************************
# Create Ramachandran plot from phi/psi data  *
#          April 2020, Slovenia               *
#**********************************************

#********************************************************
# Author: Anze Hubman                                   *
#         National Institute of Chemistry/Theory dept.  *
#********************************************************

#************************************************************************************************
# DISCLAIMER:                                                                                   *
#This code can be used and modified freely. I am not responsible for mistakes that might occur. *
#************************************************************************************************

#*****************************************************************
# Input structure                                                *
# phi space psi                                                  *
# NOTE: it is important that only 1 space separates phi and psi  *
#*****************************************************************

q = 2                                #bracket size ==> lower q means higher resolution but also higher computation time
open_i = open("rama.dat", 'r')
open_o = open("rama_hmap.dat", 'w')

#create an empty array:
arr = []
for i in range(-180+q, 181, q):
    for j in range(-180+q, 181, q):
        arr = arr + [[i, j, 0]]

#go over data:
for line in open_i:
    b = line.split(' ')
    phi = float(b[2])
    psi = float(b[3])

    for triple in arr:
        m = triple[0]
        n = triple[1]

        if (m != 180) and (n != 180) and (phi >= m-q) and (phi < m) and (psi >= n-q) and (psi < n):
            triple[2] = triple[2] + 1

        if (m == 180) and (n != 180) and (phi >= 180-q) and (phi <= 180) and (psi >= n-q) and (psi < n):
            triple[2] = triple[2] + 1

        if (m != 180) and (n == 180) and (phi >= m-q) and (phi < m) and (psi >= 180-q) and (psi <= 180):
            triple[2] = triple[2] + 1

        if (m == 180) and (n == 180) and (phi >= 180-q) and (phi <= 180) and (psi >= 180-q) and (psi <= 180):
            triple[2] = triple[2] + 1

#center and write to output file:  
for elt in arr:
    x = float(elt[0] - 0.5*q)
    y = float(elt[1] - 0.5*q)
    z = float(elt[2])
    a = str(x)
    b = str(y)
    c = str(z)
    open_o.write(a+' '+b+' '+c+'\n')
    
#NOTE: data is not normalised
open_i.close()
open_o.close()
