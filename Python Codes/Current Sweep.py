#importing all the necessary packages 

import numpy as np 
import pyvisa 
#import matplotlib.pyplot as plt 
import time 
import os 


#establishing connection with keithley 2400 which is connected in 26 th channel
rm = pyvisa.ResourceManager()
instr = rm.list_resources()
keithley = rm.open_resource('GPIB0::26::INSTR')


keithley.write("*RST")
time.sleep(0.5)
keithley.write(":ROUT:TERM FRON")

keithley.write(":SENS:FUNC:CONC OFF")
keithley.write(":SOUR:FUNC CURR")
keithley.write(":SENS:FUNC 'VOLT:DC'")
keithley.write(":SENS:VOLT:PROT 1") #compliance
keithley.write(":SOUR:CURR:START 1e-3")
keithley.write(":SOUR:CURR:STOP 10e-3")
keithley.write(":SOUR:CURR:STEP 1e-3")
keithley.write(":SOUR:CURR:MODE SWE")
keithley.write(":SOUR:SWE:RANG AUTO")
keithley.write(":SOUR:SWE:SPAC LIN")
keithley.write(":TRIG:COUN 10")
keithley.write(":SOUR:DEL 0.1")


keithley.write(":OUTP ON")
time.sleep(0.5)

keithley.write(":READ?")
#data = keithley.read_bytes(4)
time.sleep(0.5)

string_out=keithley.read()
#print( string_out)
data=string_out.split(",")
print( data )
#V,I = data[0],data[1]
#print("Voltage : ",V,"\nCurrent:",I)
time.sleep(0.5)

 
keithley.write(":OUTP OFF")


keithley.close()
