from collections import Counter

def Day3():
    input_values = LoadCsvFile()
    #print(input_values)
    gamma_rate = find_gamma_rate(input_values)
    print(f'gamma rate: {gamma_rate}')
    epsilon_rate = find_epsilon_rate(gamma_rate)
    print(f'epsilon rate: {epsilon_rate}')
    power_consumption = get_power_consumption(gamma_rate, epsilon_rate)
    print(f'Power consumption: {power_consumption}')
    #SecondHalf(df)


def find_gamma_rate(input_values):
    length = len(input_values[0])
    gamma_rate_binary = ''
    for ix in range(length):
        mode = Counter(map(lambda x: x[ix], input_values)).most_common()[0][0]
        gamma_rate_binary += mode
    return gamma_rate_binary


def find_epsilon_rate(gamma_rate_binary):
    return ''.join('1' if x == '0' else '0' for x in gamma_rate_binary)


def get_power_consumption(gamma_rate_binary, epsilon_rate_binary):
    return int(gamma_rate_binary, 2) * int(epsilon_rate_binary, 2)

def SecondHalf():
    print('Not yet implemented')

def LoadCsvFile():
    try:
        # Importing Data
        with open('input.txt') as input:
            return [x for x in input.read().split()]
    except:
        print('Error reading input file')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Day3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
