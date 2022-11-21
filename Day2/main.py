
import pandas as pd

HorizontalPosition = 0
VerticalPosition = 0


def Day2():
    df = LoadCsvFile()
    CalulatePosition(df)


def CalulatePosition(df):
    horizontalPosition = 0
    depth = 0
    index = 0

    for value in df["Direction"]:
        match value:
            case "up":
                depth = DecreaseVerticalPosition(depth, df["Distance"].iloc[index])
            case "down":
                depth = IncreaseVerticalPosition(depth, df["Distance"].iloc[index])
            case "forward":
                horizontalPosition = IncreaseHorizontalPosition(horizontalPosition, df["Distance"].iloc[index])
            case _:
                print(f'error wat')
        index = index + 1
    print(f'Horizontalposition: {horizontalPosition}')
    print(f'depth: {depth}')
    print(f'result: {horizontalPosition * depth}')


def IncreaseHorizontalPosition(horizontalPosition, value):
    return horizontalPosition + value


def IncreaseVerticalPosition(verticalPosition, value):
    return verticalPosition + value


def DecreaseVerticalPosition(verticalPosition, value):
    if (verticalPosition - value) > 0:
        verticalPosition = verticalPosition - value
    else:
        verticalPosition = 0
    return verticalPosition


def LoadCsvFile():
    try:
        return pd.read_csv("input.txt", sep=' ', names=['Direction', 'Distance'])
    except:
        print('Error reading input file')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Day2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
