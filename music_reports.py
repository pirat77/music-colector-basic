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

def report_time_range(x, y):
    report = []
    for element in readfile():
        if int(element['release year']) in range(x,y):
            report.append(element)
    return report

def sort_by_key(key):
    album_dict = readfile()
    sorted_album_dict = sorted(album_dict, key=lambda k: k[key].zfill(30))
    return sorted_album_dict


def find_albums_by_value_of_key(value, key):
    report = []
    for element in readfile():
        if value == '' or element[key].lower() == value.lower():
            report.append(element)
    return report

def find_albums_by_comprasion_of_value_key(value, key, operation):
    report = sort_by_key(key)
    if operation == 'lowest':
        return [report[0]]
    elif operation == 'highest':
        return [report[-1]]
    elif operation == 'higher':
        reportz = []
        for element in report:
            if (element[key].zfill(30)) > (value.zfill(30)):
                reportz.append(element)
        return reportz    
    elif operation == 'lower':
        reportz = []
        for element in report:
            if (element[key].zfill(30)) < (value.zfill(30)):
                reportz.append(element)
        return reportz
    
def add_album(album_data):
    album_dict = readfile()
    for element in album_dict:
        if element['album name'].lower() == album_data[1].lower():
            return 1
    path = sys.argv[0].strip("display.py")    
    f = open(path + 'text_albums_data.txt', 'a')
    f.write(','.join(album_data))
    f.close()  
    return 0




