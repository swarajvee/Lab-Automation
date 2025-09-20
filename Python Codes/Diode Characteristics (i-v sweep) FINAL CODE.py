import pyvisa         
import numpy as np
import matplotlib.pyplot as plt 
import time         
import os
import csv



#establishing connection with keithley 2400 which is connected in 26 th channel
rm = pyvisa.ResourceManager()
instr = rm.list_resources()
keithley = rm.open_resource('GPIB0::26::INSTR')




#initial voltage/ starting voltage
INITIAL_VOLTAGE = input("Enter Initial Voltage : ")
INITIAL_VOLTAGE =float(INITIAL_VOLTAGE)
INITIAL_VOLTAGE_FUNCTION = ":SOUR:VOLT:LEV "+str(INITIAL_VOLTAGE)
keithley.write(INITIAL_VOLTAGE_FUNCTION)

#maximum voltage
MAXIMUM_VOLTAGE = input("Enter Maximum Voltage : ")
MAXIMUM_VOLTAGE =float(MAXIMUM_VOLTAGE)
VOLTAGE_RANGE_FUNCTION = ":SOUR:VOLT:RANG "+str(MAXIMUM_VOLTAGE)
keithley.write(VOLTAGE_RANGE_FUNCTION)


#compliance
PROTECTION = input("Enter Compliance Value : ")
PROTECTION =float(PROTECTION)
PROTECTION_FUNCTION = ":SENS:CURR:PROT "+str(PROTECTION)
keithley.write(PROTECTION_FUNCTION)


CurrentCompliance = PROTECTION
start = INITIAL_VOLTAGE
stop =MAXIMUM_VOLTAGE


#CONFIG INSTRUMENT 
keithley.write("*RST")
time.sleep(0.5)
keithley.write(":ROUT:TERM FRON")

keithley.write(":SOUR:FUNC:MODE VOLT")
keithley.write(":SENS:CURR:PROT:LEV " + str(CurrentCompliance))
keithley.write(":SENS:CURR:RANGE:AUTO 1")   
keithley.write(":OUTP ON")


NUMBER_POINTS = input( "Enter Number of Points : " )


#for loop
Voltage=[]
Current = []
for V in np.linspace(start, stop, num=int(NUMBER_POINTS), endpoint=True):
    print("Voltage set to: " + str(V) + " V" )
    keithley.write(":SOUR:VOLT " + str(V))
    time.sleep(0.1)    
    data = keithley.query(":READ?")
    answer = data.split(',')   
    #I = float(answer[1])
    I = eval( answer.pop(1) )*1e3    
    Current.append( I )
    
    V = eval( answer.pop(0) )
    #v = float(answer[2])
    Voltage.append(V)
   
    
    print("Current = " + str(Current[-1]) + ' mA')  

    
keithley.write(":OUTP OFF")    
keithley.write("SYSTEM:KEY 23") # go to local control
keithley.close()


#saving in csv format
from itertools import zip_longest

listv=[Voltage,Current]

export_data = zip_longest(*data, fillvalue = '')
with open('I-V_observation.csv','w', newline='') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(listv)
    write.writerows(export_data)
    
    
    
csv_file.close()    
    
#value plotting    
plt.plot(Voltage,Current)
plt.title("Diode I-V Characteristics")
plt.xlabel("voltage ( V )",color='green')
plt.ylabel("Current ( mA )",color='green')
plt.show()
