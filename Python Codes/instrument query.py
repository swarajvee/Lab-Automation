'''#contacting the SMU 
import pyvisa 
rm = pyvisa.ResourceManager()
instr = rm.list_resources()
print ( instr ) # shows all the available instrument
'''

import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()
my_instrument = rm.open_resource('GPIB0::26::INSTR')
print ( my_instrument.query('*IDN?'))


