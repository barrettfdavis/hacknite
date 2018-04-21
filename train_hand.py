import serial
import keyboard
import pandas as pd
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
        while ((len(trial)) < 99): #store (100 * #inputs) data points

            s = ser.readline()              # read in arduino serial output
            s = s.decode('utf-8')
            s = s.trim(',')



            trial.append(s) # decode byte literal to string

        saveQ = input('Save training data? [y/n] ')
        if saveQ == 'y':
            print('Trial data saved to training set')
            train.append(trial)
        else:
            print('Trial data not saved')

        print('Press ''a'' to record, ''f'' to save and quit... ')

    elif command == ('f'): # for saving training data

        df = pd.DataFrame(train)
        gesture = input('What gesture was that? ')

        with open(gesture + '.csv', 'w') as f:
            df.to_csv(f, index=False, header=False)

        train = [] #clear out the cache
        print('saved!')
