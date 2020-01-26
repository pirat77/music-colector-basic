from music_reports import *
import shutil
import os





def print_center_list(input_list):
    os.system("clear")
    columns = shutil.get_terminal_size().columns
    for element in input_list:
        for elementx in element:
            print((str(elementx) + ' : ' + str(element[elementx])).center(columns))
        print()



print_center_list(find_albums_by_value_of_key('pop', 'genre'))

