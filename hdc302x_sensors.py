#HDC302x Sensor Grain Probe V.1
#About: Gathers Data from the HDC302x (We Are Using HDC3022) Temperature Sensors
#Created: 5/21/2026
#Micro Controller: Raspberry Pi Pico W
#Interpreter: MicroPython
#Main Code: hdc302x_sensor.py
#Last Edit: NolanRH on 5/27/2026

#hdc302x_sensor.py Imports
from machine import Pin, I2C
import utime, time
import hdc302x_library #Library Import (hdc302x_library.py)

#Class Allows Import of all Included Functions
class HDC302X_Sensors:
    #I2C Buses
    i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000) #I2C Bus 0 (GP1=SCL, GP0=SDA)
    i2c1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000) #I2C Bus 1 (GP3=SCL, GP2=SDA)
    
    bus0 = [
        ("Sensor 1", "x044", hdc302x_library.HDC302X(i2c0, address=0x44)), #Sensor 1
        ("Sensor 2", "x045", hdc302x_library.HDC302X(i2c0, address=0x45)), #Sensor 2
        ("Sensor 3", "x046", hdc302x_library.HDC302X(i2c0, address=0x46)), #Sensor 3
        ("Sensor 4", "x047", hdc302x_library.HDC302X(i2c0, address=0x47))] #Sensor 4
    bus1 = [
        ("Sensor 5", "x044", hdc302x_library.HDC302X(i2c1, address=0x44)), #Sensor 5
        ("Sensor 6", "x045", hdc302x_library.HDC302X(i2c1, address=0x45)), #Sensor 6
        ("Sensor 7", "x046", hdc302x_library.HDC302X(i2c1, address=0x46)), #Sensor 7
        ("Sensor 8", "x047", hdc302x_library.HDC302X(i2c1, address=0x47))] #Sensor 8
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEBUGGING FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~(Functions Should be put in Main Loop to Debug)~~~~~~~~~~~~~~~~~~~~~~#
    @staticmethod 
    def debug_readings():
        timestamps = []
        #Debug Print for Bus 0
        sensorsBus0 = []
        addrsBus0 = []
        tempsBus0 = []
        humiditiesBus0 = []
        for i, (sensor_name, addrs, sensor) in enumerate(HDC302X_Sensors.bus0):
            try:
                temp = sensor.temperature
                hum = sensor.relative_humidity
                sensorsBus0.append(sensor_name)
                addrsBus0.append(addrs)
                tempsBus0.append(temp)
                humiditiesBus0.append(hum)
                now = time.localtime() #To Accurately Timestamp Each Sensor Separately, Must Copy to Each Enumeration of Try/Except
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                timestamps.append(times)
            except Exception as e:
                #print(f"{sensor_name} ERROR:", e) #Exeception Error Print
                sensorsBus0.append(sensor_name)
                addrsBus0.append(addrs)
                tempsBus0.append(0.0)
                humiditiesBus0.append(0.0)
                now = time.localtime() #To Accurately Timestamp Each Sensor Separately, Must Copy to Each Enumeration of Try/Except
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                timestamps.append(times)
        #Debug Print for Bus 1
        sensorsBus1 = []
        addrsBus1 = []
        tempsBus1 = []
        humiditiesBus1 = []
        for i, (sensor_name, addrs, sensor) in enumerate(HDC302X_Sensors.bus1):
            try:
                temp = sensor.temperature
                hum = sensor.relative_humidity
                sensorsBus1.append(sensor_name)
                addrsBus1.append(addrs)
                tempsBus1.append(temp)
                humiditiesBus1.append(hum)
                now = time.localtime() #To Accurately Timestamp Each Sensor Separately, Must Copy to Each Enumeration of Try/Except
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                timestamps.append(times)
            except Exception as e:
                #print(f"{sensor_name} ERROR:", e) #Exeception Error Print
                sensorsBus1.append(sensor_name)
                addrsBus1.append(addrs)
                tempsBus1.append(0.0)
                humiditiesBus1.append(0.0)
                now = time.localtime() #To Accurately Timestamp Each Sensor Separately, Must Copy to Each Enumeration of Try/Except
                times = ("{:04d}-{:02d}-{:02d} " "{:02d}:{:02d}:{:02d}").format(now[0], now[1], now[2], now[3], now[4], now[5], now[6], now[7])
                timestamps.append(times)
        
        print(f"\n================================SENSOR LOGGER================================")
        print(f"---BUS 0---")
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus0[0], addrsBus0[0], tempsBus0[0], humiditiesBus0[0], timestamps[0])) #Bus 0 Sensor 1 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus0[1], addrsBus0[1], tempsBus0[1], humiditiesBus0[1], timestamps[1])) #Bus 0 Sensor 2 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus0[2], addrsBus0[2], tempsBus0[2], humiditiesBus0[2], timestamps[2])) #Bus 0 Sensor 3 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus0[3], addrsBus0[3], tempsBus0[3], humiditiesBus0[3], timestamps[3])) #Bus 0 Sensor 4 Log
        print(f"---BUS 1---")
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus1[0], addrsBus1[0], tempsBus1[0], humiditiesBus1[0], timestamps[4])) #Bus 1 Sensor 5 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus1[1], addrsBus1[1], tempsBus1[1], humiditiesBus1[1], timestamps[5])) #Bus 1 Sensor 6 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus1[2], addrsBus1[2], tempsBus1[2], humiditiesBus1[2], timestamps[6])) #Bus 1 Sensor 7 Log
        print("{} ({}): Temperature = {:.2f}°C  |  Humidity = {:.1f}%  |  {}".format(sensorsBus1[3], addrsBus1[3], tempsBus1[3], humiditiesBus1[3], timestamps[7])) #Bus 1 Sensor 8 Log
        utime.sleep(1.0) #Delay in Seconds (Repeats the Debug Prints this Often)
