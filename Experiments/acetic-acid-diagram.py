import matplotlib.pyplot as plt
   
time = [0,10,20,30,40,50,60,70,80,90,100,110]
AOS = [0.236115,0.207933182,0.202933182,0.200205905,0.197933182,0.196115,0.194296818,0.192933182,0.192024091,0.190660455,0.189751364,0.188387727]
  
plt.plot(time, AOS)
plt.title('Amount of Substance (CH3COOH)-Time-Diagram')
plt.xlabel('Time [s]')
plt.ylabel('Amount of Substance [mol]')
plt.show()
