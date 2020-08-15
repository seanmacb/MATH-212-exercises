#Eulers approximation of Capybara's getting eaten by jaguars. Nom nom nom.
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

h=0.01
alpha=0.8
beta=0.05
gamma=0.85
delta=0.02


def main():
    xold=100
    yold=30
    told=0
    capylist=[]
    jaglist=[]
    tlist=[]
    tlist.append(told)
    capylist.append(xold)
    jaglist.append(yold)    
    for t in range(0,int(24/h)):
        x=h*(xold*(alpha-beta*yold))+xold
        y=h*(yold*(delta*xold-gamma))+yold
        t=told+h
        capylist.append(x)
        xold=x
        jaglist.append(y)
        yold=y
        tlist.append(t)
        told=t
    #Plot of Jaguars pop vs time and Capybaras pop vs. time. Blue is jaguars, orange is capybaras 
    plt.plot(tlist,jaglist)
    plt.plot(tlist,capylist)
    plt.grid("True")
    plt.xlabel("t (Months)")
    plt.ylabel("Capybaras (Orange) & Jaguars (Blue)")
    plt.show()
    plt.close()
    
    #Plot of Jaguars vs capybaras
    plt.plot(capylist,jaglist)
    plt.grid("True")
    plt.xlabel("Capybaras")
    plt.ylabel("Jaguars")
    plt.show()
    plt.close()
    #First two values
    print("Capybara first two values:", capylist[1:3])
    print("Jaguar first two values:", jaglist[1:3])    
main()

'''

Run this for the graphs of time vs. capylist and jaglist

In the time vs. Capybara and jaguar pop graph, the capybara population initally decreases as the jaguars eat them, then the jaguar population decreases due to the lack of capybaras. This results in the capybara population increasing. This occurs periodically, and both populations increase in every time period.

In the capybaras vs. jaguars graph, you can see a stable ecosystem, which would increase in total population over time.

'''
