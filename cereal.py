from time import sleep
import serial




#Arduino Serial Read

outF = open('testoutput.txt','w')

ser = serial.Serial('/dev/cu.wchusbserial1410', 115200)
while True:
    s = ser.readline()
    s = s.decode("utf-8")

    s = s.split(",")
    s = s[:-1]

    arr = [int(x) for x in s]
    print(arr)
    """
    print(s)
    #print(s, file = outF)
    """

#Training
