# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import decimal
decimal.getcontext().prec = 100
import matplotlib.pyplot as pp
import math 

#LB and UB are the lower and upper bounds of a given problem
#nvars variables
#Npop streams created
#Nsr best rivers
#dmax = 0.0000000000000001 #1e -16 small numbre "close" to 0, the smaller the more search intensity
#Maxit max iterations 1000
def WCA(function,xLB,xUB,nvars,Npop,Nsr,dmax,max_it):
    

    def objective_function(var):

        if function == 'Bukin':
            x1 = var[0]
            x2 = var[1]
            term1 = 100 * ((abs(x2 - (0.01*x1**2)))**1/2)
            term2 = 0.01 * abs(x1+10)
            res = term1 + term2
            return res
        if function == 'GRIEWANK':
            sums = 0
            prod = 1
            for i in range(0,len(var)):
                xi = var[i]
                sums = sums + (xi) ** 2 / 4000
                prod = prod * math.cos(xi/math.sqrt(i+1))
            res = sums - prod + 1
            return res     
        if function == 'ACKLEY':
            a = 20
            b = 0.2
            c = 6.283185307
            sum1 = 0
            sum2 = 0
            d = len(var)
            for i in range(0,len(var)):
                xi = var[i]
                sum1 = sum1 + xi**2
                sum2 = sum2 + math.cos(c*xi)
            term1 = -a * math.exp(-b*math.sqrt(sum1/d))
            term2 = -math.exp(sum2/d)
            res = term1 + term2 + a + math.exp(1)
            return res     
        if function == 'RASTRIGIN':
            sum1 = 0
            d = len(var)
            for i in range(0,len(var)):
                xi = var[i]
                sum1 = sum1 + (xi**2 - 10*math.cos(2*math.pi*xi))
            res = 10*d + sum1
            return res     
        if function == 'ROTATED HYPER-ELLIPSOID':
            outer = 0
            d = len(var)
            for i in range(0,d):
                inner = 0
                for j in range(0,i):
                    xj = var[j]
                    inner = inner + xj**2
                outer = outer + inner     
            
            res = outer
            return res     
        if function == 'SPHERE':
            d = len(var);
            sum1 = 0;
            for i in range(0,len(var)):
                xi = var[i]
                sum1 = sum1 + xi**2;
            res = sum1
            return res
        if function == 'DIXON-PRICE':
            x1 = var[0]
            d = len(var)
            term1 = (x1-1)**2
            sum1 = 0
            for i in range(1,len(var)):
                xi = var[i]
                xold = var[i-1]
                new = i * (2*xi**2 - xold)**2
                sum1 = sum1 + new
            res = term1 + sum1
            return res
        if function == 'SUM SQUARES':
            d = len(var)
            sum1 = 0
            for i in range(0,len(var)):
                xi = var[i]
                sum1 = sum1 + i*xi**2
            res = sum1
            return res
        if function == 'TRID':
            d = len(var)
            sum1 = (var[0]-1)**2
            sum2 = 0
            for i in range(1,len(var)):
                xi = var[i]
                xold = var[i-1]
                sum1 = sum1 + (xi-1)**2
                sum2 = sum2 + xi*xold
            res = sum1 - sum2
            return res
        if function == 'ROSENBROCK':
            x = var
            res = sum([100*(x[i+1] - x[i]**2)**2 + (x[i] - 1)**2 for i in range(len(x)-1)])
            """
            d = len(var);
            sum1 = 0;
            for i in range(0,len(var)-1):
                xi = var[i]
                xnext = var[i+1]
                new = 100*(xnext-xi**2)**2 + (xi-1)**2
                sum1  = sum1 + new
            res = sum1 
            """
            return res
        if function == 'LEVY':
            d = len(var);
            w =[]

            for i in range(0,d):
                w.append( 1 + (var[i] - 1)/4)
            
            term1 = math.sin(math.pi*w[1])**2
            term3 = (w[d-1]-1)**2 * (1+(math.sin(2*math.pi*w[d-1]))**2)
            sum1 = 0
            
            for i in range(0,len(var)-1):
                wi = w[i]
                xnext = var[i+1]
                new = (wi-1)**2 * (1+10*(math.sin(math.pi*wi+1))**2)
                sum1 = sum1 + new
            res = term1 + sum1 + term3
            
            return res

    N_stream = Npop-Nsr

#0 position(variables created),  1 cost(funtion values with the created value)
   
    
    def mainPopulation():
        global  pop,sea,river,streams
        pop = [[],[]]
        for i in range(0, Npop):
            dArray = []
            for j in range(0,nvars):
                x = round(xLB + ( xUB - xLB ) * rd.random(),10)
                dArray.append(x)      
            pop[0].append(dArray)
            pop[1].append(objective_function(pop[0][i]))
    
    
        a = np.array(pop[1])
        b = np.sort(a)#sort the array
        idx = np.argsort(a)#get index of array
        c = np.array(pop[0])#assign the index to the variables
        pop[0] = c[np.argsort(idx)]
        pop[1] = b
    
    
        sea =[[],[]]
        #Forming Sea best solution
        sea = [pop[0][0],pop[1][0]]
       
        #Forming Rivers, best NSR, solutions
        river=[[],[]]
    
        for i in range(1, Nsr):
            river[0].append(pop[0][i])    
            river[1].append(pop[1][i])
        
       
            
        #Stream
        streams=[[],[]]
        for i in range(Nsr, N_stream+Nsr):
            streams[0].append(pop[0][i])    
            streams[1].append(pop[1][i])
    
    
    
       #designate streams -> rivers -> sea
       #From the shortest stream, goes through the rivers to get to the sea
       
       #Cs contains the results of the sea, rivers and first stream
        global cs, ns, cn
       
        cs = [sea[1]]
        
        for j in range(0,len(river[1])):
            cs.append(river[1][j])
        
        cs.append(streams[1][0])    
        
        maxVal = max(cs)
    
        cn=[]
        for u in range(0, len(cs)):
            cn.append(cs[u] - maxVal)
    
    
        ns = cn
        sumOne = sum(cn)
        for k in range(0, len(ns)):    
            ns[k] =round( abs(cn[k]/sumOne) * N_stream)
        #ns contains the deignated flows from stream to sea-river
        #Example [2,2,2,1,0]
        #2 streams go to the sea
        #2 streams go to the river1
        #2 streams go to the river2
        #1 streams go to the river3
        
    
      #modification on NS
        idx = Nsr
    
        while sum(ns) > N_stream:
            if ns[idx] > 1:
                ns[idx]= ns[idx]-1
            else:
                idx = idx-1
    
        
      
        idx=1;
        while sum(ns)<N_stream:
            ns[idx] = ns[idx]+1
            
        del(ns[-1])
        return ns

    #Nsr valor de 40 aprox para que  no de 0
    ns = mainPopulation()
    zeroCheck= True  
    while zeroCheck:
        if 0 in ns:
            zeroCheck = True
            ns = mainPopulation()         
        else:
            zeroCheck = False


    ns = sorted(ns, reverse=True) #for sea too
    nb = ns[1:] #only for rivers
    
    #Water cycle ALgorithm iteration 

    plotArray =[]
    #Main loop´iterations

    def check(list_):
        boolCheck = False
        for item in list_:
            if item  < xLB or item > xUB:
                boolCheck = True
        return boolCheck
    
    
    for i in range(0,max_it):
        
        #Stream to the sea, repeat the times of the     2 streams go to the sea
        for sPos in range(0, ns[0]):
            f = float('{0:.3g}'.format(rd.uniform(0, 1)))
            streams[0][sPos] = streams[0][sPos] + (2 * f) * (sea[0]-streams[0][sPos])
            whileCheck = check(streams[0][sPos])
            while whileCheck:
                f = float('{0:.3g}'.format(rd.uniform(0, 1)))
                streams[0][sPos] = streams[0][sPos] + (2 * f) * (sea[0]-streams[0][sPos])
                whileCheck = check(streams[0][sPos])
            
            

            streams[1][sPos] = round(objective_function(streams[0][sPos]),10)    

   
            #Check new better solution
            #print(sea)

            if streams[1][sPos] < sea[1]:
                newSea=[[],[]]
                newSea[0] = streams[0][sPos]
                newSea[1] = streams[1][sPos]
                streams[0][sPos] = sea[0]
                streams[1][sPos] = sea[1]
                sea[0] = newSea[0]
                sea[1] = newSea[1]
                #print('mejoro ')
            #print('ultimo: ' ,sea)


        #Stream to sea, 3 times repeat if 4 
        for i in range(0, Nsr-1):
            for j in range(0, nb[i]):
                f = float('{0:.3g}'.format(rd.uniform(0, 1)))
                streams[0][j+sum(ns[1:i])] = (streams[0][j+sum(ns[1:i])])+ (2 * f)*(river[0][j]-streams[0][j+sum(ns[1:i])])
                whileCheck = check(streams[0][j+sum(ns[1:i])])
                while whileCheck:
                    f = float('{0:.3g}'.format(rd.uniform(0, 1)))
                    streams[0][j+sum(ns[1:i])] = (streams[0][j+sum(ns[1:i])])+ (2 * f)*(river[0][j]-streams[0][j+sum(ns[1:i])])
                    whileCheck = check(streams[0][j+sum(ns[1:i])])
                
       
                streams[1][j+sum(ns[1:i])]=round(objective_function(streams[0][j+sum(ns[1:i])]),10)
                

                if streams[1][j+sum(ns[1:i])] < river[1][j]:
                    newRiver = [[],[]]
                    newRiver[0].append(streams[0][j+sum(ns[1:i])])
                    newRiver[1].append(streams[1][j+sum(ns[1:i])])
                    streams[0][j+sum(ns[1:i])] = river[0][j]
                    streams[1][j+sum(ns[1:i])] = river[1][j]
                    river[0][j] = newRiver[0][0]
                    river[1][j] = newRiver[1][0]
                    
                if river[1][j]< sea[1]:
                    newSea=[[],[]]
                    newSea[0] = river[0][j]
                    newSea[1] = river[1][j]
                    river[0][j] = sea[0]
                    river[1][j] = sea[1]
                    sea[0] = newSea[0]
                    sea[1] = newSea[1]

        #River to the sea
        for j in range(0,Nsr-1):
            f = float('{0:.3g}'.format(rd.uniform(0, 1)))  
            river[0][j]= (river[0][j]) + (2 * f)*(sea[0]-river[0][j])
            whileCheck = check(river[0][j])
            while whileCheck:
                f = float('{0:.3g}'.format(rd.uniform(0, 1)))
                river[0][j]= (river[0][j]) + (2 * f)*(sea[0]-river[0][j])
                whileCheck = check(river[0][j])


            river[1][j]=round(objective_function(river[0][j]),10)


            if river[1][j]< sea[1]:
                newSea=[[],[]]
                newSea[0] = river[0][j]
                newSea[1] = river[1][j]
                river[0][j] = sea[0]
                river[1][j] = sea[1]
                sea[0] = newSea[0]
                sea[1] = newSea[1]
                
        #Evaporation condition for rivers and sea

        for k in range(0, Nsr-1):
            if np.linalg.norm(river[0][k]-sea[0]) < dmax or f < 0.1:
                for j in range(0,nb[k]):  
                    dArray = []
                    for j in range(0,nvars):
                        x = round(xLB + ( xUB - xLB ) * rd.random(),10)
                        dArray.append(x)      
                    streams[0][j+sum(ns[1:k])] = dArray 


        for j in range(0, ns[1]):
            #Evaporation condition for rivers and sea
            if np.linalg.norm(streams[0][j]-sea[0]) < dmax:
                    dArray = []
                    for j in range(0,nvars):
                        x = round(xLB + ( xUB - xLB ) * rd.random(),10)
                        dArray.append(x)     
                    streams[0][j] = dArray 



     
        dmax = dmax -(dmax/max_it)
        #print('function  ',sea[1])
        plotArray.append(sea[1])
    #print('array final ',plotArray)
    
    ar = plotArray
    NFEs=Npop*max_it;
    Xmin=sea[0];
    Fmin=objective_function(Xmin);
    print('NFES  ',NFEs)
    print('variables: ',Xmin)
    print('f(x) minimo: ',Fmin)
    pp.plot(ar, np.zeros_like(ar) +0, 'x')
    pp.show()    
    return Fmin    
        