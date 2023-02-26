# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Storage logging example"""
import time
import board
import digitalio
import adafruit_dotstar as dotstar
import adafruit_bno055_short_version

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_bno055_short_version.BNO055(i2c)
dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# For most CircuitPython boards:
# led = digitalio.DigitalInOut(board.LED)
# led.switch_to_output()

# rollUp_MagOffsetX = 0
# mCounter = 0
# storageTime = 10



# try :
#     f = open("/mag_offSet.txt", "r")    # start with reading the calibration 
#     CalibrationList = f.read()          # store the data in a list    
#     f.close                             # close the file
#     dots[0] = (0,224,0)                 # the second N sets the intesity of the green color      
# except :
#     dots[0] = (224,0,0)                 # the first N sets the intesity of the red color  
    

#sensor.Set_Offset(CalibrationList) # push the value in the registers

while True:
    print("Calibration GYR ACC MAG:  {} ".format(sensor.calibration_status) , "Heading :  {:.0f} ".format(sensor.eulReadings))
    sensor.mode = 0b0000 # the sensor have to be in config mode if we are to be able to read the offset settings 

    CalibAggegationList = sensor.CalibrationOffSet
    # here we need to try the setter
    
    sensor.CalibrationOffSet=CalibAggegationList


    sensor.mode = 0b1100
    print()
    time.sleep(1)
    mCounter = mCounter +1
    if mCounter == storageTime :             
        with open("/mag_offSet.txt", "w") as fp:
            #fp.write('{0:f}\n'.format(CalibAggegationList))
            fp.write(CalibAggegationList)
            fp.flush()                
        mCounter = 0


