import argparse
import random
import math
import sys
import os

class Syntheticfier():
    def __init__(self, size):
        self.seed = 7
        self.path = "synthetic/"
        self._random_data = self.create_random_data([size], self.seed)[0]

    def modify_data(self, input_data, position, percentage, type_of_change):
        random.seed(self.seed)
        data = list(input_data)

        len_of_change = math.ceil(len(data) / 100 * percentage)
        if len_of_change > len(data):
            len_of_change = len(data)

        section_size = int(len(data) / 3)
        if position == 'first':
            pos = random.randint(0, section_size)
        elif position == 'second':
            pos = random.randint(section_size, 2 * section_size)
        elif position == 'third':
            pos = random.randint(2 * section_size, 3 * section_size)
        else:
            pos = random.randint(0, len(data))
        if pos + len_of_change >= len(data):
            pos -= (pos + len_of_change - len(data))
            if pos < 0:
                pos = 0
        
        if type_of_change == 'change':
            ret_data = data.copy()
            ret_data[pos:pos+len_of_change] = self._random_data[0:len_of_change]
        elif type_of_change == 'delete':
            ret_data = data[0:pos]
            ret_data.extend(data[pos+len_of_change::])
        else:
            rand_data = self._random_data[0:len_of_change]
            ret_data = data[0:pos]
            ret_data.extend(rand_data)
            ret_data.extend(data[pos::])
        return bytearray(ret_data)

    @staticmethod
    def create_original_data(sizes, seed):
        random.seed(seed)
        data_list = list()
        for size in sizes:
            data = list()
            for i in range(0,size):
                data.append(random.getrandbits(8))
            with open("synthetic/original/original_random_data_%s" % (size), 'wb') as newFile:
                newFile.write(bytearray(data))
            data_list.append(data)
        return data_list

    @staticmethod
    def create_random_data(sizes, seed):
        random.seed(seed)
        data_list = list()
        for size in sizes:
            data = list()
            for i in range(0,size):
                data.append(random.getrandbits(8))
            data_list.append(data)
        return data_list


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bytes', help='sizes in bytes of the synthetic files', default=[1000,10000,100000,1000000,10000000], nargs='+', type=int)
    parser.add_argument('-s', '--steps', help='manipulation steps', default=1, type=int)
    args = parser.parse_args()
    return args.bytes, args.steps

def main():
    sizes, steps = get_arguments()
    modifier = Syntheticfier(max(sizes))

    if not os.path.exists("synthetic"):
        os.makedirs("synthetic/original")

    for j,data in enumerate(modifier.create_original_data(sizes, 8)):
        for i in range(0,101,steps):
            if not os.path.exists("synthetic/delete/first/%s" % sizes[j]):
                os.makedirs("synthetic/delete/first/%s" % sizes[j])
                os.makedirs("synthetic/delete/second/%s" % sizes[j])
                os.makedirs("synthetic/delete/third/%s" % sizes[j])
            modified_data = modifier.modify_data(bytearray(data), 'first', i, 'delete')
            with open("synthetic/delete/first/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)
            modified_data = modifier.modify_data(bytearray(data), 'second', i, 'delete')
            with open("synthetic/delete/second/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)
            modified_data = modifier.modify_data(bytearray(data), 'third', i, 'delete')
            with open("synthetic/delete/third/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)

            if not os.path.exists("synthetic/insert/first/%s" % sizes[j]):
                os.makedirs("synthetic/insert/first/%s" % sizes[j])
                os.makedirs("synthetic/insert/second/%s" % sizes[j])
                os.makedirs("synthetic/insert/third/%s" % sizes[j])
            modified_data = modifier.modify_data(bytearray(data), 'first', i, 'insert')
            with open("synthetic/insert/first/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)
            modified_data = modifier.modify_data(bytearray(data), 'second', i, 'insert')
            with open("synthetic/insert/second/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)
            modified_data = modifier.modify_data(bytearray(data), 'third', i, 'insert')
            with open("synthetic/insert/third/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)

            if not os.path.exists("synthetic/change/first/%s" % sizes[j]):
                os.makedirs("synthetic/change/first/%s" % sizes[j])
                os.makedirs("synthetic/change/second/%s" % sizes[j])
                os.makedirs("synthetic/change/third/%s" % sizes[j])
            modified_data = modifier.modify_data(bytearray(data), 'first', i, 'change')
            with open("synthetic/change/first/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)
            modified_data = modifier.modify_data(bytearray(data), 'second', i, 'change')
            with open("synthetic/change/second/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)
            modified_data = modifier.modify_data(bytearray(data), 'third', i, 'change')
            with open("synthetic/change/third/%s/%s" % (sizes[j],i), 'wb') as newFile:
                newFile.write(modified_data)

if __name__ == "__main__":
    main()
