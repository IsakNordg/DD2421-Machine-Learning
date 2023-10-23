import re

class Data():
    def __init__(self) -> None:
        self.datapoints = {}

    def read_data(self):
        # data file contains index,y,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13
        first = True

        with open('trainOnMe.csv', 'r') as f:
            for line in f:
                if first:
                    first = False
                    continue
                line = line.split(',')
                self.datapoints[int(line[0])] = line[1:]


    def clean_data(self):
        for key, value in self.datapoints.items():
            for i in range(len(value)):
                #if value[i] == 'NA':
                #    value[i] = '0'
                if value[i] == 'True':
                    value[i] = '1'
            self.datapoints[key] = value

    def write_data(self):
        with open('cleanedData.csv', 'w') as f:
            for key, value in self.datapoints.items():
                f.write(str(key) + ',' + ','.join(value))

if __name__ == '__main__':
    data = Data()
    data.read_data()
    data.clean_data()
    data.write_data()

    for key, value in data.datapoints.items():
        for i in range(len(value)):
            if re.search("[a-zA-Z]", value[i]) and i != 0 and i != 7:
                print(key, i, value[i])
        