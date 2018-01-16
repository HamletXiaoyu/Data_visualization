#coding=utf-8
#数据可视化：编写一个程序，对于给定的一组数据和要求，输出一个以字符组成的柱状图
import sys


class Data_info:
    def __init__(self, max_value, max_len):
        self._max_value, self._max_len = max_value, max_len
        
def get_data_info(diction):
    # max value
    max_value = diction[max(diction, key=lambda x: diction[x])]
    # longest name's length
    max_len = len(max(diction, key=lambda x: len(x)))
    return Data_info(max_value, max_len)

def sort_data(diction, option):
    items = []
    if option == "Value":# sort by value
        items = sorted(diction.items(), key=lambda d: d[1])
    else:                # sort by name
        items = sorted(diction.items(), key=lambda d: d[0])
    return items
    
def show(items, option, info):
    row = len(items) * 2 + 1
    idx = 0
    for i in range(row):
        if i == 0:
            line = '\u250c' + '\u2500' * info._max_len + '\u252c' + '\u2500' * 20 + '\u2510'
            print(line.decode('unicode_escape'))
        elif i == row - 1:
            line = '\u2514' + '\u2500' * info._max_len + '\u2534' + '\u2500' * 20 + '\u2518'
            print(line.decode('unicode_escape'))
        elif i % 2 == 0:
            line = '\u251c' + '\u2500' * info._max_len + '\u253c' + '\u2500' * 20 + '\u2524'
            print(line.decode('unicode_escape'))                
        else:
            if option == "ASC":  # ascend order
                length = int(float(items[idx][1]) / info._max_value * 20.0)
                line = '\u2502' + '\u0020' * (info._max_len - len(items[idx][0])) + items[idx][0] + \
                       '\u2502' + '\u2588' * length + '\u0020' * (20 - length) + '\u2502'
                idx += 1
                print(line.decode('unicode_escape'))
            else:                # descend order
                length = int(float(items[-1-idx][1]) / info._max_value * 20.0)
                line = '\u2502' + '\u0020' * (info._max_len - len(items[-1 - idx][0])) + items[-1 - idx][0] + \
                       '\u2502' + '\u2588' * length + '\u0020' * (20 - length) + '\u2502'
                idx += 1
                print(line.decode('unicode_escape'))

    
def main():
    try:
        # input count of data
        while(True):
            count = int(sys.stdin.readline().strip('\n'))
            if count < 1 or count > 20:
                print("Error input, expect a integer N (1<=N<=20).\nPlease input again!")
            else:
                break
            
        # input sorting options
        while(True):
            sort_options = sys.stdin.readline().split()
            if len(sort_options) != 2 or ("Value" not in sort_options and "Name" not in sort_options) \
               or ("ASC" not in sort_options and "DESC" not in sort_options):
                print("Error input, expect: Value/Name DESC/ASC!\nPlease input again!")
            else:
                break

        # input data
        contains = {}
        for i in range(count):
            while(True):
                temp_input = sys.stdin.readline().split()
                if len(temp_input) != 2:
                    print("input error, expect : name value!\nPlease input again!")
                else:
                    break
            contains[temp_input[0]] = int(temp_input[1])
            
        # sort contains
        items = sort_data(contains, sort_options[0])
        
        # get max length and max value in contains
        info_of_contains = get_data_info(contains)
        
        # show table
        show(items, sort_options[1], info_of_contains)
        
    except ValueError as error:
        print(error)
    
if __name__ == '__main__':
    main()
