# Development of Open-Source Python Program for Lab Automation

## Project Overview
This project develops an open-source Python program to automate a Keithley 2400 Source Measure Unit (SMU) for performing I-V characterization of electronic components like silicon diodes and LEDs. The goal is to replace expensive proprietary software (e.g., LabVIEW) with a free, accessible, and customizable Python-based solution.

## Hardware Requirements
- Keithley 2400 SMU
- GPIB to USB Interface (e.g., Keithley KUSB-488B)
- Silicon Diode and LED (as DUTs)
- Computer with USB port

## Software Requirements
- Python 3.7+
- Python packages: `pyvisa`, `numpy`, `matplotlib`, `time`, `os`, `csv`
- Keithley KUSB-488B Driver
- NI-VISA Library

## Installation Steps
1. Install Python 3.7 or later from [python.org](https://python.org)
2. Install required Python packages: `pip install pyvisa numpy matplotlib`
3. Download and install the KUSB-488B driver from the Keithley website
4. Download and install the NI-VISA Library from the National Instruments website

## Connection Setup
1. Connect the GPIB interface to the Keithley 2400 SMU and the computer via USB
2. Connect the device under test (DUT) to the SMU’s front terminals (HI and LO)
3. Verify the GPIB connection using the device manager (green indicator should light up)

## Usage
1. Run the Python script: `python keithley_iv_measurement.py`
2. Follow the prompts to enter compliance current, initial/maximum voltage, number of points, and component name
3. The script will perform a voltage sweep, measure current, save data to a CSV file, and plot the I-V curve

## Example Output
- CSV file: `I_V_Observation_<component_name>.csv`
- Plot: I-V characteristics graph

## Code Structure
- Import required libraries
- Establish GPIB connection
- Configure SMU settings
- Perform voltage sweep and current measurement
- Save and plot data

## References
- Keithley 2400 User Manual
- PyVISA Documentation
- NI-VISA Resources

## License
This project is open-source and available under the MIT License.

## Author
Swaraj V, Department of Physics, Cochin University of Science and Technology, July 2022
