# -*- coding: utf-8 -*-

#rom WCA import WCA
from WCAloop import WCA



#def WCA(function,xLB,xUB,yLB,yUB,nvars,Npop,Nsr,dmax,max_it):

#Two variables working fine, the more dimensions, the error increases
#WCA('GRIEWANK',-600,600,-3,3,2,10,4,0.0000000000000001,600)

#10 dimensions 

"""
#Ackley function 
AckleyRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('LEVY',-32.768,32.768,10,50,13,0.0000000000000001,1600)
        except:
            pass
    AckleyRes = AckleyRes + result
    
print('         ') 
print('Promedio',AckleyRes/30)     
"""
"""
#Griewank function 
grieRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('GRIEWANK',-600,600,10,55,12,0.0000000000000001,1200)
        except:
            pass
    grieRes = grieRes + result
    
print('         ') 
print('Promedio',grieRes/30) 
"""
"""
#Rastrigin function 
rastRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('RASTRIGIN',-5.12,5.12,10,55,13,0.0000000000000001,2500)
            #WCA('RASTRIGIN',-5.12,5.12,3,16,6,0.0000000000000001,1500)
        except:
            pass
    rastRes = rastRes + result
    
print('         ') 
print('Promedio',rastRes/30)   

"""
""" 
#ROTATED HYPER-ELLIPSOID function 
rotedRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('ROTATED HYPER-ELLIPSOID',-65.536,65.536,10,55,12,0.0000000000000001,1200)
        except:
            pass
    rotedRes = rotedRes + result
    
print('         ') 
print('Promedio',rotedRes/30)     
"""
"""
#Sphere function 
sphRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('SPHERE',-10,10,10,55,12,0.0000000000000001,1200)
        except:
            pass
    sphRes = sphRes + result
    
print('         ') 
print('Promedio',sphRes/30)
"""
"""
#dix function 
dixRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('DIXON-PRICE',-10,10,10,55,12,0.0000000000000001,1200)
        except:
            pass
    dixRes = dixRes + result
    
print('         ') 
print('Promedio',dixRes/30)     
"""
"""
#SUM SQUARES function 
sumssRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('SUM SQUARES',-5.12,5.12,10,55,12,0.0000000000000001,1200)
        except:
            pass
    sumssRes = sumssRes + result
    
print('         ') 
print('Promedio',sumssRes/30)     
"""


#ROSENBROCK function 
"""
rosenRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('ROSENBROCK',-5,10,10,55,12,0.0000000000000001,1200)
            #WCA('ROSENBROCK',-5,5,10,55,12,0.0000000000000001,1200)
        except:
            pass
    rosenRes = rosenRes + result
    
print('         ') 
print('Promedio',rosenRes/30)
"""
"""
#Trid function 
tridRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('TRID',-100,100,10,55,12,0.0000000000000001,1200)
        except:
            pass
    tridRes = tridRes + result
    
print('         ') 
print('Promedio',tridRes/30)     

"""
"""
#Levy function 
LevyRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('LEVY',-10,10,10,55,12,0.0000000000000001,1200)
        except:
            pass
    LevyRes = LevyRes + result
    
print('         ') 
print('Promedio',LevyRes/30)     
"""


#20 dimensioines 
"""
#Ackley function 
ackRes = 0
for i in range(0,10):
    result = None
    while result is None:
        try:
            result = WCA('ACKLEY',-32.768,32.768,20,140,22,0.0000000000000001,1200)
        except:
            pass
    ackRes = ackRes + result
    
print('         ') 
print('Promedio',ackRes/10) 
"""
"""
#Griewank function 
grieRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('GRIEWANK',-600,600,20,140,22,0.0000000000000001,1200)
        except:
            pass
    grieRes = grieRes + result
    
print('         ') 
print('Promedio',grieRes/30) 
"""

#Rotated Hyper Ellipsoid function 
"""
rotRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('ROTATED HYPER-ELLIPSOID',-65.536,65.536,20,140,22,0.0000000000000001,1200)
        except:
            pass
    rotRes = rotRes + result
    
print('         ') 
print('Promedio',rotRes/30) 
"""
"""
#Sphere function
ssRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('SPHERE',-10,10,20,140,22,0.0000000000000001,1200)
        except:
            pass
    ssRes = ssRes + result
    
print('         ') 
print('Promedio',ssRes/30) 
"""
"""
#Dixon-Price function
dxpRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('DIXON-PRICE',-10,10,20,140,22,0.0000000000000001,1200)
        except:
            pass
    dxpRes = dxpRes + result
    
print('         ') 
print('Promedio',dxpRes/30) 
"""
"""
#Rastrigin function
rasRes = 0
for i in range(0,8):
    result = None
    while result is None:
        try:
            result = WCA('RASTRIGIN',-5.12,5.12,20,140,22,0.0000000000000001,1200)
        except:
            pass
    rasRes = rasRes + result
    
print('         ') 
print('Promedio',rasRes/8)
""" 
"""
#Rosenbrock function
rosRes = 0
for i in range(0,8):
    result = None
    while result is None:
        try:
            result = WCA('ROSENBROCK',-5,10,20,140,22,0.0000000000000001,2200)
        except:
            pass
    rosRes = rosRes + result
    
print('         ') 
print('Promedio',rosRes/8) 

"""
"""
#Trid function
triRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('TRID',-400,400,20,140,22,0.0000000000000001,4500)
        except:
            pass
    triRes = triRes + result
    
print('         ') 
print('Promedio',triRes/30) 
"""
"""
#LEVY function
levRes = 0
for i in range(0,30):
    result = None
    while result is None:
        try:
            result = WCA('LEVY',-10,10,20,140,22,0.0000000000000001,4500)
        except:
            pass
    levRes = levRes + result
    
print('         ') 
print('Promedio',levRes/30)
"""

