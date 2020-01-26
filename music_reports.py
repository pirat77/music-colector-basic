import sys
import re

def readfile():
    path = sys.argv[0].strip("display.py")
    data_structure = ['artist name', 'album name', 'release year', 'genre', 'lenght']
    albums_dict =[]
    with open(path + 'text_albums_data.txt', 'r') as f:
        albums_list = f.readlines()
    for element in albums_list:
        albums_dict.append(dict(zip(data_structure, element.strip("\n").split(','))))
    return albums_dict

def report_albums():
    report = []
    for element in readfile():
        report.append(element)
    return report

def report_genre(album_genre):
    report = []
    for element in readfile():
        if element['genre'] == album_genre:
            report.append(element)
    return report

def report_time_range(x, y):
    report = []
    for element in readfile():
        if int(element['release year']) in range(x,y):
            report.append(element)
    return report

def sort_by_lenght():
    album_dict = readfile()
    sorted_album_dict = sorted(album_dict, key=lambda k: k['lenght'].zfill(7))
    return sorted_album_dict

def report_artist(artist_name):
    report = []
    for element in readfile():
        if element['artist name'] == artist_name:
            report.append(element)
    return report

def find_album_by_name(album_name):
    


