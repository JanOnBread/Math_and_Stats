
"""
Plot Recamán's sequence as semicircles (Python)
"""

# Importing modules 
import numpy as np
import matplotlib.pyplot as plt

def plot_squence_as_semicircle(k):

    """
    Plots the sequence with term x_k, k being our input, as semicircles
    jumping from each term. 
    """

    # Forming our sequence 
    x=[0]
    for i in range (1, k + 1):
            if x[i-1] - i > 0 and  x[i-1] - i  not in x:
                    x.append( x[i-1] - i)
            else:
                    x.append ( x[i-1] + i)
    

    def draw_semicircle (a,b):
        """
        Draws a semicircle with the centre (|a+b|/2, 0) where a and b are the 
        start and end x values of the semi-circle. 
        """
        ax = plt.subplot(111)
        
        #Finds our radius (r), range between our a and b (p), centre (h)
        r = np.abs(a - b) / 2   
        p = np.linspace(a, b, 10000)  
        h = (b + a) /2    
        
        # Plugs r, p, h into our rearrange circle formula to find our y 
        y = np.sqrt(r**2 - (p - h)**2) 
        
    
        # Plots semicircles 

        # Drawn over or under semi circles depending on the iteration (i)
        plt.rcParams["figure.figsize"] = (18,10)
        if i % 2 != 0 : 
            ax.plot(p, -y, color = "black", linewidth=1)
        else:
             ax.plot(p, y, color= "black", linewidth=1)
        ax.plot(a, 0, "o", color= "blue", markersize=3)
        ax.plot(b, 0, "o", color= "blue", markersize=3)

        # If this is our last semicircle, we plot the axis. 
        if i == k -1:

            # Labling axix and font siz
            plt.rc('font', size = 18)   
            plt.gca().set_aspect('equal', adjustable = 'box')
            plt.xlabel("$x_n$", fontsize = 28)
            plt.title("Sequence up n = {}". format (k), fontsize = 20)
            
            # Removing grids
            ax.tick_params(labelleft = False)
            ax.tick_params(left = False)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
        
    # Loop to plot each of out semi cicles 
    for i in range (0,k):
        draw_semicircle(x[i], x[i+1])
