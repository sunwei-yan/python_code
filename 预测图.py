from pickletools import pydict
import numpy
import matplotlib.pyplot as plt


y=[11.90,13.27,14.57,13.03,13.83,11.99,13.57,12.64,10.86,11.41,9.52]
x=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline=numpy.linspace(2010,2030,10)
plt.scatter(x,y)
plt.title("Birth rate prediction")

plt.plot(myline,mymodel(myline))

plt.show()