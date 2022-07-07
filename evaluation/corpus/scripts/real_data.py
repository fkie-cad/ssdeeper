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


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) != 4:
        print('Usage: {prog} FILE SECTION MODIFICATION'.format(prog=argv[0]))
        return 1
    section = argv[2]
    mod = argv[3]
    data = open(argv[1], 'rb').read()
    modifier = Syntheticfier(len(data))

    for i in range(0,101,1):
        if not os.path.exists("real/%s/%s/" % (mod,section)):
            os.makedirs("real/%s/%s/" % (mod,section))
        modified_data = modifier.modify_data(bytearray(data), section, i, mod)
        with open("real/%s/%s/%s" % (mod,section,i), 'wb') as newFile:
            newFile.write(modified_data)


if __name__ == "__main__":
    main()
