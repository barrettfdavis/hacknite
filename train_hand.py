import serial
import keyboard
import pandas as pd
import numpy as np
import time
import csv


#Arduino Serial Read
ser = serial.Serial('/dev/cu.wchusbserial1410', 115200)
train = []

print('Press ''a'' to record, ''f'' to save and quit... ')

while True:

    command = input()

    if command == 'a':  # for training
        trial = []
        while ((len(trial)) < 10): #store (100 * #inputs) data points

              s = ser.readline()
              s = s.decode("utf-8")

              s = s.split(","); s = s[:-1] # revise later
              arr = [int(x) for x in s]

              trial.append(arr) # decode byte literal to string

        saveQ = input('Save training data? [y/n] ')
        if saveQ == 'y':
            print('Trial data saved to training set')
            train = train + trial
        else:
            print('Trial data not saved')

        print('Press ''a'' to record, ''f'' to save and quit... ')

    elif command == ('f'): # for saving training data

        gesture = input('What gesture was that? ')

        """
        with open(gesture + '.csv', 'w') as f:
            aout = np.asarray(train)
            np.savetxt(f,aout,delimiter = ",")

        gesture = input('What gesture was that? ')
        df = pd.DataFrame(train)
        df.to_csv(f, index=False, header=False)
        #print(df)
        """
        with open(gesture + '.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(train)


        train = [] #clear out the cache
        print('saved!')
