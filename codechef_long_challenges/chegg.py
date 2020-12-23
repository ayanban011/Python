import math
import matplotlib.pyplot as plt
def make_packet(x0,k0,sigma):
    X=[]
    Y=[]
    for i in range(1,101):
        X.append(i)
        y= ((1/2*3.14*(sigma**2))**0.25)*(math.exp(-(i-x0)**2/4*sigma**2))*(math.exp(-1**0.5*k0*i))
        Y.append(y**2)
    plt.plot(X,Y)
make_packet(20,2,2)
