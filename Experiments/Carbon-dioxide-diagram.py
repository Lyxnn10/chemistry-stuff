import matplotlib.pyplot as plt
   
time = [0,10,20,30,40,50,60,70,80,90,100,110]
AOS = [0,0.014090909,0.016590909,0.017954545,0.019090909,0.02,0.020909091,0.021590909,0.022045455,0.022727273,0.023181818,0.023863636]
  
plt.plot(time, AOS)
plt.title('Amount of Substance (CO2)-Time-diagram')
plt.xlabel('Time [s]')
plt.ylabel('Amount of Substance [mol]')
plt.show()
