import scipy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data/km_year_power_price.csv")
parameters=["km","year","powerPS"]


for param in parameters:
    fig,ax = plt.subplots()
    ax.scatter(data[param],data["avgPrice"],label="Data",s=4)
    z = scipy.stats.linregress(data[param],data["avgPrice"])
    description = "Fitted line with parameters:\nSlope: "+"{:.2f}".format(z[0])+"\nIntercept: "+"{:.2f}".format(z[1])+"\nrvalue: "+"{:.2f}".format(z[2])
    x =[x for x in np.linspace(np.min(data[param]),np.max(data[param]),1000)]
    y =[z[0]*x+z[1] for x in x]
    ax.plot(x,y,label=description,color="orange")
    print("Regression with param " + param + ": " + str(z))
    print("\n-----------------------------------\n")
    ax.set_xlabel(param)
    ax.set_ylabel("avgPrice")
    ax.legend()
plt.show()