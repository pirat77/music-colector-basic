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



#print(report_albums())
#print(report_genre('pop'))
#print(report_time_range(1990, 2000))
#print(sort_by_lenght())
print_center_list(report_artist('Pink Floyd'))
