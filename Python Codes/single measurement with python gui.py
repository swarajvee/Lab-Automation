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

#maximum voltage
MAXIMUM_VOLTAGE = input("Enter Maximum Voltage : ")
VOLTAGE_RANGE_FUNCTION = ":SOUR:VOLT:RANG "+MAXIMUM_VOLTAGE
keithley.write(VOLTAGE_RANGE_FUNCTION)

#initial voltage/ starting voltage
INITIAL_VOLTAGE = input("Enter Initial Voltage : ")
INITIAL_VOLTAGE_FUNCTION = ":SOUR:VOLT:LEV "+INITIAL_VOLTAGE
keithley.write(INITIAL_VOLTAGE_FUNCTION)


keithley.write(':SENS:FUNC "CURR"')

#compliance
PROTECTION = input("Enter Compliance Value : ")
PROTECTION_FUNCTION = ":SENS:CURR:PROT "+PROTECTION
keithley.write(PROTECTION_FUNCTION)

#measuring current range
OUTPUT_CURRENT_RANGE = input("Enter Sensing Current Range : ")
OUTPUT_CURRENT_RANGE_FUNCTION =":SENS:CURR:RANG "+OUTPUT_CURRENT_RANGE
keithley.write(OUTPUT_CURRENT_RANGE_FUNCTION)



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
