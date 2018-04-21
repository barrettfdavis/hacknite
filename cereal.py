from time import sleep
import serial




#Arduino Serial Read
ser = serial.Serial('/dev/cu.wchusbserial1410', 115200)
while True:
    s = ser.readline()
    s = s.decode("utf-8")
    s = s.rstrip(',')
    list(s)
    print(s)




#Training
