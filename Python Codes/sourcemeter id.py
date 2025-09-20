#import pyvisa
from pymeasure.instruments.keithley import Keithley2400

#rm = pyvisa.ResourceManager()
#print(rm.list_resources())

sourcemeter = Keithley2400("GPIB::26")
print(sourcemeter.id)
