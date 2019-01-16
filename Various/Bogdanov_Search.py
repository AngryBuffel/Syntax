# VDLS - 15/01/19 - Bogdanov Search Update.

# TODO: Explicit is better than implicit.

import numpy as np
from numpy.lib.scimath import *
import random
import time

# TODO: Redefine functions.
def user_input():
    # Global Variables Declaration
    global y_,t_,k_,d_,E_,M_,n_iter,num_div
    # Array initialization with number of iterations.
    n_iter = int(input('How many iterations will be used for the convergence test?\t'))
    y_ = np.zeros(n_iter); t_ = np.zeros(n_iter)
    # Number of interval divisions.
    num_div = int(input('\nHow many equidistant divisions you want for the intervals?\t'))
    num_div = num_div + 1 #fix for index notation
    print ('\n\tAll of the variables values and intervals are set by default...')
    set_int = input('Do you want to set the intervals for each variable? (y/n)\t').strip().lower()
    # Default intervals
    if set_int == 'n':
        y_[0] = round(random.uniform(-0.6,1.0),2); t_[0] = round(random.uniform(-0.7,0.9),2)
        d_ = float(1.0189); M_ = np.linspace(-0.5,0.5, num_div) #d_ is fixed. 
        k_ = np.linspace(0.05,0.34, num_div); E_ = np.linspace(-0.02,0.02, num_div)
    # User intervals
    elif set_int == 'y':
        y_[0] = float(input('Introduce the inital value for y_0:\t'))
        t_[0] = float(input('Introduce the inital value for theta_0:\t'))
        # TODO: Replace by a dictionary and/or a single for loop?
        map_vars = ['k','M','E']
        intervals = []
        for var in map_vars:
            intervals.append(float(input('Introduce intial point for ' + var + ' interval:\t')))
            intervals.append(float(input('Introduce final point for ' + var + ' interval:\t')))
        print(intervals)
        k_ = np.linspace(intervals[0],intervals[1], num_div)
        M_ = np.linspace(intervals[2],intervals[3], num_div)  #swap for M_
        E_ = np.linspace(intervals[4],intervals[5], num_div)
        d_ = float(input('Introduce the inital value for d_:\t'))
    # Exit
    else:                   
        quit('--- Invalid Choice, Program End. ---')
    # Is this return necessary if all variables are global?
    return y_,t_,k_,d_,E_,M_,n_iter,num_div

# Math Function definitions
# TODO: Replace for lambda functions.

def gamma(y_,t_,k_,d_,E_,M_):
    global gamasg
    ym1=y_-1
    ym12=ym1*ym1
    gamasg=t_*(-12*(k_**2)*y_*ym12 + t_*(36*(k_**2)*(d_**2)*ym12 + \
    (2+E_+M_*y_)**2 -12*k_*(ym1)*(1+E_+M_*y_+d_*(-1+E_+M_*y_))))
    return sqrt(gamasg)

def nu(y_,t_,k_,d_,E_,M_):
    ym1=y_-1
    return t_*(8+E_+12*k_*d_*(ym1)+M_*y_)
    
def phi(y_,t_,k_,d_,E_,M_):
    ym1=y_-1
    return -t_*(2+E_+3*k_*d_*(ym1)+M_*y_)
    
def rho(y_,t_,k_,d_,E_,M_):
    ym1=y_-1
    return t_*(-4-5*E_+12*k_*d_*(ym1)-5*M_*y_)

# Matrix elements as functions

def a_elem(y_,t_,k_,d_,E_,M_):
    return (nu(y_,t_,k_,d_,E_,M_) + gamma(y_,t_,k_,d_,E_,M_))/(6*t_)
    
def b_elem(y_,t_,k_,d_,E_,M_):
    return (phi(y_,t_,k_,d_,E_,M_) - gamma(y_,t_,k_,d_,E_,M_))/(3*k_*t_*(y_-1))
    
def c_elem(y_,k_):
    return k_*(1-y_)
    
def e_elem(y_,t_,k_,d_,E_,M_):
    return (rho(y_,t_,k_,d_,E_,M_) + gamma(y_,t_,k_,d_,E_,M_))/(6*t_)

# ------------------------------------------------------------------------------------
# Main program body.
# TODO: Improve user input.
# TODO: Replace all trivial type changes.
# TODO: Turn this into a function.
user_input()

print ('\ny_0 = {y:4.2f}, theta_0 = {t:4.2f}. \n'.format(y=y_[0],t=t_[0]))

print('Searching for values...\n')

# Iteration loops, i,j,l,n,p are iteration indexes
# TODO: Turn iteration loop into a function.
c2_ = 0 #tuple counter init
t0 = time.perf_counter()

for i in list(range(0,num_div)):
    for j in list(range(0,num_div)):
        for l in list(range(0,num_div)):
            
            c_ = 0 # Counter init for iteration loop
                
            for p in list(range(1,n_iter)): #Main iteration loop
                    
                pm1 = p-1
                                       
                y_[p] = y_[pm1]*a_elem(y_[pm1],t_[pm1],k_[i],d_,E_[l],M_[j]) + \
                            t_[pm1]*b_elem(y_[pm1],t_[pm1],k_[i],d_,E_[l],M_[j])
                            
                t_[p] = y_[pm1]*c_elem(y_[pm1],k_[i]) + \
                            t_[pm1]*e_elem(y_[pm1],t_[pm1],k_[i],d_,E_[l],M_[j])
                    
                ay = abs(y_[p])
                aty= abs(t_[p])
                    
                c_ += 1
                    
    #Condiciones para encontrar valores
                # TODO: np.select()    
                if c_ >= (n_iter - 1):
                    filename = 'fixed_d_search.txt'
                    with open(filename, 'a') as file_object:
                        file_object.write(str(y_[0])+','+str(t_[0])+','+str(k_[i])+','+str(d_)+','+str(E_[l])+','+str(M_[j])+'\n')
                        #(y_[0],t_[0],k_,d_,E_,M_) tuple to unpack when file is read.
                        c2_ += 1

                elif b_elem(y_[pm1],t_[pm1],k_[i],d_,E_[l],M_[j]) < 0:
                    break
                elif ay==0. or aty ==0.:
                    break
                elif gamasg < 0.: #y_,t_ reales
                    break
                elif abs(y_[p] - y_[pm1]) > 10 or abs(t_[p] - t_[pm1]) > 10:
                    break
                #elif b_elem(y_[pm1],t_[pm1],k_[i],d_,E_[l],M_[j]) >= d_0:
                #    break

t1 = time.perf_counter()
tf = float(t1 - t0); ns=num_div**3; print('\n\t{nc:} combinations were searched in {tt:7.2f} seconds.\n'.format(nc=ns,tt=tf))
                        
if c2_ > 0:
    print('\t\t'+str(c2_)+' tuples were found!!!\n')
else:
    print('\t\t\tNo tuples were found. :c\n\t\t\t\tTry again!!!\n')

print('\t-----\t-----\t-----\tPROGRAM END\t-----\t-----\t-----')