import sys
import re



def readfile():
    path = sys.argv[0].strip("music_reports.py")
    data_structure = ['artist name', 'album name', 'release year', 'genre', 'length']
    albums_dict =[]
    with open(path + 'text_albums_data.txt', 'r') as f:
        albums_list = f.readlines()
    for element in albums_list:
        albums_dict.append(dict(zip(data_structure, element.strip("\n").split(','))))
    return albums_dict

print(readfile())


