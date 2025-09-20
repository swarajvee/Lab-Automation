#importing all the necessary packages 

import numpy as np 
import pyvisa 
import matplotlib.pyplot as plt 
import time 
import os 


#establishing connection with keithley 2400 which is connected in 26 th channel
rm = pyvisa.ResourceManager()
instr = rm.list_resources()
keithley = rm.open_resource('GPIB0::26::INSTR')


keithley.write("*RST")
time.sleep(0.5)
keithley.write(":ROUT:TERM FRON")

keithley.write(":SOUR:FUNC VOLT")
keithley.write(":SOUR:CURR:MODE FIX")

MAXIMUM_VOLTAGE = input("Enter Maximum Voltage : ")
VOLTAGE_RANGE_FUNCTION = ":SOUR:VOLT:RANG "+MAXIMUM_VOLTAGE
keithley.write(VOLTAGE_RANGE_FUNCTION)
keithley.write(":SOUR:VOLT:LEV 10")


keithley.write(':SENS:FUNC "CURR"')
keithley.write(":SENS:CURR:PROT 10e-3")
keithley.write(":SENS:CURR:RANG 10e-3")
#keithley.write("[:SENS]:CURR:RANG:AUTO OFF")
#keithley.write(":SENS:CURR:RANG 10e-3")

keithley.write(":OUTP ON")
time.sleep(0.5)

keithley.write(":READ?")
#data = keithley.read_bytes(4)
time.sleep(0.5)

string_out=keithley.read()
#print( string_out)
data=string_out.split(",")
V,I = data[0],data[1]
print("Voltage : ",V,"\nCurrent:",I)
time.sleep(0.5)

 
keithley.write(":OUTP OFF")


keithley.close()
