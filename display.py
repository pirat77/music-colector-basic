from music_reports import *
import shutil
import os



def main():
    action = ''
    while action == '':    
        terminal = [{'Author': 'Jan Mikos', 'Program': 'Music Collector', 'Ver.': '0.7', 'actions': 'add album, edit album, list albums, exit'}]
        print_center_list(terminal)
        print('\n')
        action = input('Choose your action: ')
        print('\n')
        if action.lower() == 'add album':            
            add_album(gather_album_data())
        elif action.lower() == 'edit album':
            album_name = input('Album name: ')
            album_data = find_albums_by_value_of_key(album_name, 'album name')
            if album_data:
                print(album_data)
                edit_album(album_name, gather_album_data())
            else: print('No such album in the list :(')


def print_center_list(input_list):
    os.system("clear")
    columns = shutil.get_terminal_size().columns
    for element in input_list:
        for elementx in element:
            print((str(elementx) + ' : ' + str(element[elementx])).center(columns))
        print()

main()

# edit_album('Low', ['David Bowie','High','1977','rock','38:26'])

# print_center_list(find_albums_by_comprasion_of_value_key('high', 'album name', 'highest'))

