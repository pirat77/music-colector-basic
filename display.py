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


add_album(['Paktofonika', 'Kinematografia', '1999', 'hip hop', '44:44'])
print_center_list(find_albums_by_comprasion_of_value_key('44:45', 'lenght', 'lower'))

