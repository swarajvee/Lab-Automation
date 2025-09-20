#VOLTAGE SWEEP 

import numpy as np 
import pyvisa 
import matplotlib.pyplot as plt 
import time 
import os 


#establishing connection with keithley 2400 which is connected in 26 th channel
rm = pyvisa.ResourceManager()
instr = rm.list_resources()
keithley = rm.open_resource('GPIB0::26::INSTR')

#config source measure function 
keithley.write("*RST")
time.sleep(0.5)
keithley.write(":ROUT:TERM FRON")

keithley.write(":SOUR:FUNC VOLT")
keithley.write(':SENS:FUNC "CURR"')
keithley.write(":SENS:CURR:PROT 10e-3")



#config sweep


keithley.write(":SOUR:SWE:SPAC LIN") #ENABLED LINEAR SWEEP
keithley.write(":SOUR:VOLT:STAR 10")
keithley.write(":SOUR:VOLT:STOP 21")
keithley.write(":SOUR:VOLT:STEP 1")
keithley.write(":SOUR:VOLT:MODE SWE")
keithley.write(":SOUR:SWE:RANG FIX")
keithley.write(":SOUR:SWE:DIR UP")
#time.sleep(0.5)

keithley.write(":TRIG:COUN 10")#

keithley.write(":SOUR:SWE:CAB EARL")


#DELAY TIME
keithley.write(":SOUR:DEL 0.1")

#OUTPUT ON
keithley.write(":OUTP ON")
time.sleep(0.5)


#RUN SWEEP

#keithley.write(":READ?")





#string_out=keithley.read()
string_out=keithley.query(":READ?")
print(keithley.write(":FORM:ELEM CURR"))
print(type((string_out)))
time.sleep(0.5)
keithley.write(":OUTP OFF")




#
voltages = keithley.query_ascii_values("trace:data?")
print("Average voltage: ", sum(voltages) / len(voltages))



keithley.query("status:measurement?")
keithley.write("trace:never; trace:clear; feed:control next")




