import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/frontLegSensorValues.npy')
sinusoidalValuesBl = numpy.load('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/sinusoidalValuesBl.npy')
sinusoidalValuesFl = numpy.load('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/sinusoidalValuesFl.npy')

#matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg', linewidth=4)
#matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg')
matplotlib.pyplot.plot(sinusoidalValuesBl, linewidth=4)
matplotlib.pyplot.plot(sinusoidalValuesFl)


matplotlib.pyplot.legend()
matplotlib.pyplot.show()