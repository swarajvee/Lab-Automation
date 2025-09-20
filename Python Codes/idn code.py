import pyvisa
inst = pyvisa.ResourceManager().list_resources('GPIB0::26::INSTR')
print(inst.query("*IDN?"))
