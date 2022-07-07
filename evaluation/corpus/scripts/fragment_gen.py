import argparse
import random
import math
import sys
import os


class Modifier():
    def __init__(self, size):
        random.seed(7)
        self.seed = 7
        self._random_data = self.create_random_data([size], self.seed)[0]
        pass

    def modify_data(self, input_data, position, percentage, type_of_change):
        random.seed(7)
        data = list(input_data)
        len_of_change = math.ceil(len(data) / 100 * percentage)
        if len_of_change > len(data):
            len_of_change = len(data)
        part_c = int(len(data) / 3)
        if position == 'first':
            pos = random.randint(0, part_c)
        elif position == 'second':
            pos = random.randint(part_c, 2 * part_c)
        elif position == 'third':
            pos = random.randint(2 * part_c, 3 * part_c)
        else:
            pos = random.randint(0, len(data))
        if pos + len_of_change >= len(data):
            pos =- (pos + len_of_change - len(data))
            if pos < 0:
                pos = 0
        if type_of_change == 'change':
            ret_data = data.copy()
            ret_data[pos:pos+len_of_change] = self._random_data[0:len_of_change]
        elif type_of_change == 'delete':
            ret_data = data[0:pos]
            ret_data.extend(data[pos+len_of_change::])
            #print(data)
            #print(ret_data)
        else:
            rand_data = self._random_data[0:len_of_change]
            ret_data = data[0:pos]
            ret_data.extend(rand_data)
            ret_data.extend(data[pos::])
        return bytearray(ret_data)

    def modify_random_data(self, input_data, percentage, type_of_change):
        pos = 0
        data = list(input_data)
        len_of_change = math.ceil(len(data) / 100 * percentage)
        if len_of_change > len(data):
            len_of_change = len(data)
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
    def create_random_data(sizes, seed):
        random.seed(seed)
        data_list = list()
        for size in sizes:
            data = list()
            for i in range(0,size):
                data.append(random.getrandbits(8))
            data_list.append(data)
        return data_list


def main():
    random.seed(7)
    modifier = Modifier(10000000)
    A = [95, 90, 75, 50, 25]
    for file in os.listdir("t5-corpus-roussev"):
        for i in A:
            if not os.path.exists("t5-fragments/%s" % i):
                os.makedirs("t5-fragments/%s" % i)
        
            data = open("t5-corpus-roussev/"+file, 'rb').read()
            modified_data = modifier.modify_data(bytearray(data), 'first', i, 'delete')
            newFile = open("t5-fragments/%s/first_0%s_delete_%s" % (i,i,file), "wb")
            newFile.write(modified_data)

            data = open("t5-corpus-roussev/"+file, 'rb').read()
            modified_data = modifier.modify_data(bytearray(data), 'second', i, 'delete')
            newFile = open("t5-fragments/%s/second_0%s_delete_%s" % (i,i,file), "wb")
            newFile.write(modified_data)

            data = open("t5-corpus-roussev/"+file, 'rb').read()
            modified_data = modifier.modify_data(bytearray(data), 'first', i, 'delete')
            newFile = open("t5-fragments/%s/third_0%s_delete_%s" % (i,i,file), "wb")
            newFile.write(modified_data)


if __name__ == '__main__':
    sys.exit(main())
