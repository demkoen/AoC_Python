# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

HorizontalPosition = 0
VerticalPosition = 0

def Day2():
    df = LoadCsvFile()
    #print(df.to_string())
    CalulatePosition(df)

def CalulatePosition(df):
    horizontalPosition = 0
    verticalPosition = 0
    index = 0

    for value in df.iterrows('Distance'):
        print(f'value on line is: {df['Direction'].iloc[index]}')
        index = index + 1

def IncreaseHorizontalPosition(horizontalPosition, value):
    if (horizontalPosition + value) <= 0:
        horizontalPosition = horizontalPosition + value
    else:
        horizontalPosition = 0
    return horizontalPosition

def DecreaseHorizontalPosition(horizontalPosition, value):
    return horizontalPosition - value

def IncreaseVerticalPosition(verticalPosition, value):
    if (verticalPosition + value) <= 0:
        verticalPosition = verticalPosition + value
    else:
        verticalPosition = 0
    return verticalPosition

def DecreaseVerticalPosition(verticalPosition, value):
    return verticalPosition - value

def LoadCsvFile():
    try:
        return pd.read_csv("input.txt",sep=' ', names=['Direction', 'Distance'])
    except:
        print('Error reading input file')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Day2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
