#Main Grain Probe V.1
#About: Main Code Loop for the Grain Probe Project
#Created: 4/6/2026
#Micro Controller: Raspberry Pi Pico W
#Interpreter: MicroPython
#Main Code
#main.py
#Last Edit: NolanRH on 5/27/2026

#Credit
#If Labelled 'Debug Execution Timer' then it was copied from 'How to measure EXECUTION TIME in Python ⌚' by 'Bro Code' on YouTube

#Project .py Imports
from hdc302x_sensors import HDC302X_Sensors

#main.py Imports
import utime, time

#Main Loop
while True:
    start_timer = time.ticks_us() #Debug Execution Timer
    
    #----------------------------------------------------------------------------------------------------------------------
    #Debugging Functions
    HDC302X_Sensors.debug_readings() #Calls a hdc302x_sensor.py Debug Function
    #----------------------------------------------------------------------------------------------------------------------
    
    end_timer = time.ticks_us() #Debug Execution Timer
    elapsed_time = end_timer - start_timer #Debug Execution Timer
    
    print(f"\n================================MAIN LOOP LOG================================")
    print(f"Execution Time: {elapsed_time/1000000:.5f} seconds") #Debug Execution Timer
    print('Main Loop Executed Successfully!\n') #Debug Print
    
    #Creates a Delay Before Running the Next Iteration of the Main Loop
    utime.sleep(5.0) #Delay in Seconds (Change this to Shorten/Lengthen Time between Samples)
