#HDC302x Sensor Grain Probe V.1
#About: Gathers Data from the HDC302x (We Are Using HDC3022) Temperature Sensors
#Created: 5/21/2026
#Micro Controller: Raspberry Pi Pico W
#Interpreter: MicroPython
#Main Code
#hdc302x_sensor.py
#Last Edit: NolanRH on 5/21/2026

#hdc302x_sensor.py Imports
from machine import Pin, I2C
import utime, time

#Class Allows Import of all Included Functions
class HDC302X_Sensors:
    #I2C Buses
    i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000) #I2C Bus 0 (GP1=SCL, GP0=SDA)
    i2c1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000) #I2C Bus 1 (GP3=SCL, GP2=SDA)

    #Sensor Addresses
    bus0_addrs = [0x44, 0x45, 0x46, 0x47]
    bus1_addrs = [0x44, 0x45, 0x46, 0x47]

    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    #HDC302x Helper Functions (Not my Code so I'll need to go Through and Figure out what it's doing)
    #HDC302x Reader
    @staticmethod #Defines a Method that Belongs to a Class but Does Not Require an Instance of that Class to Run
    def read_hdc302x(i2c, addr): #Trigger Measurement (Command from Datasheet)
        i2c.writeto(addr, b'\x24\x00')  #High Repeatability Measurement

        time.sleep_ms(20)

        data = i2c.readfrom(addr, 6) #Combines the Most/Least Significant Bytes to Create Full 16 Bit Number

        temp_raw = (data[0] << 8) | data[1] #Takes Raw Temperature Data 0-65535
        hum_raw  = (data[3] << 8) | data[4] #Takes Raw Humidity Data 0-65535

        temperature = -45 + (175 * (temp_raw / 65535)) #Converts Raw Temperature into Celsius
        humidity = 100 * (hum_raw / 65535) #Converts Raw Humidity into Humidity Percentage

        return temperature, humidity
    '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

    #Debugging Functions (Functions Should be put in Main Loop to Debug)
    #Function to Debug Sensor Readings
    @staticmethod 
    def debug_readings():
        #Debug Print for Bus 0
        print("Bus 0")
        for i, addr in enumerate(HDC302X_Sensors.bus0_addrs):
            try:
                temp, hum = HDC302X_Sensors.read_hdc302x(HDC302X_Sensors.i2c0, addr)
                print(f"Sensor {i+1} (0x{addr:02X})") #Sensor Address
                print(f"Temperature: {temp:0.1f} C") #Temperature Reading
                print(f"Relative Humidity: {hum:0.1f} %\n") #Humidity Reading
            except Exception as e:
                print(f"Sensor {i+1} error:", e) #Exeception Error Print
        #Debug Print for Bus 1
        print("Bus 1")
        for i, addr in enumerate(HDC302X_Sensors.bus1_addrs):
            try:
                temp, hum = HDC302X_Sensors.read_hdc302x(HDC302X_Sensors.i2c1, addr)
                print(f"Sensor {i+5} (0x{addr:02X})") #Sensor Address
                print(f"Temperature: {temp:0.1f} C") #Temperature Reading
                print(f"Relative Humidity: {hum:0.1f} %\n") #Humidity Reading
            except Exception as e:
                print(f"Sensor {i+5} error:", e) #Exeception Error Print
        print("=====================================")
        utime.sleep(1.0) #Delay in Seconds (Repeats the Debug Prints this Often)