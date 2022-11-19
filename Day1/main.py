# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def Day1():

    df = LoadCsvFile()
    #print(df.to_string())
    increasements = calculateDeptIncreasement(df)
    print(f'amount of increasements is {increasements}')

def LoadCsvFile():
    try:
        return pd.read_csv("input.txt", names=['Dept'])
    except:
        print('Error reading input file')

def calculateDeptIncreasement(df):
    increaseCounter = 0
    index = 0
    comparedept = int(df.iloc[0])
    for i, row in df.iterrows():
       if int(df.iloc[index]) > comparedept:
            #print(f'dept {int(df.iloc[index])} is bigger then previous dept {comparedept}')
            increaseCounter = increaseCounter + 1
       comparedept = int(df.iloc[index])
       index = index + 1
    return increaseCounter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Day1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
