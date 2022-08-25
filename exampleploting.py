
#https://youtu.be/UO98lJQ3QGI
#,line graf

from matplotlib import pyplot as plt

#print(plt.style.available)
#plt.style.use('fivethirtyeight')#ggplot

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]

plt.plot(ages_x,dev_y, lable='All Devs',marker='.',linestyle='--',color='#444444')

py_dev_y = [41496,48800,53852,57220,63010,65990,70006,70028,71497,75378,83642]

plt.plot(ages_x,py_dev_y, lable='Python',marker='o',linewidth=3,color='#5a7d9a')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by age')

plt.legend()#(['ALL Devs','Python'])

plt.grid(True)

plt.tight_layout()#,padding

plt.show()




