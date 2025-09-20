import pyvisa          # PyVISA module, for GPIB comms
import numpy as N    # enable NumPy numerical analysis
import time          # to allow pause between measurements
import os            # Filesystem manipulation - mkdir, paths etc.

import matplotlib.pyplot as plt # for python-style plottting, like 'ax1.plot(x,y)'

Keithley_GPIB_Addr = 26
# Open Visa connections to instruments
#keithley = visa.GpibInstrument(22)     # GPIB addr 22
rm = pyvisa.ResourceManager()
keithley = rm.list_resources(  'GPIB::' + str(Keithley_GPIB_Addr)  )
print( keithley )
