from sklearn import svm
import pandas as pd
from sklearn import datasets

# Sample iris dataset
iris = datasets.load_iris()

# Define main() function
def main():
    # Loop until user finishes entering categories and quits
    targets = []
    target = input("Enter target name, or enter \"done\" to quit adding targets: ")
    while True:
        if target == 'done':
            break
        else:
            targets.append(target)
            target = input()
    for target in targets:
        try:
            data = load(target)
            print(data)
        except FileNotFoundError:
            print("File for target \"" + target + "\" not found")


def load(target):
    # Load .csv file for "close" gesture
    # Add extention
    target = target + ".csv"
    # Attempt to open file of category name
    raw_data = open(target, 'r')
    # Create list to contain values from file
    structured_data = []
    # Add each row from CSV
    for line in raw_data:
        line = line[:-1]
        line = line.split(",")
        structured_data.append(line)
    raw_data.close()
    structured_data = pd.DataFrame(structured_data)
    # Return final array
    return structured_data


# Call main() function
main()
