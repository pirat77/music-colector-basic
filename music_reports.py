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
    f.write('\n')
    f.close()  
    return 0

def edit_album(album_name, album_data):
    path = sys.argv[0].strip("display.py")    
    album_dict = readfile()
    for element in album_dict:
        if element['album name'].lower() == album_name.lower():
            element['artist name'] = album_data[0]
            element['album name'] = album_data[1]
            element['release year'] = album_data[2]
            element['genre'] = album_data[3]
            element['lenght'] = album_data[4]
    f = open(path + 'text_albums_data.txt', 'w')
    for element in album_dict:
        album_data[0] = element['artist name']
        album_data[1] = element['album name']
        album_data[2] = element['release year']
        album_data[3] = element['genre']
        album_data[4] = element['lenght']
        f.write(','.join(album_data))
        f.write('\n')
    f.close()

def gather_album_data():
    artist_name = ''
    album_name = ''
    release_year = ''
    genre = ''
    lenght = ''
    while artist_name == '':
        artist_name = input('Artist Name: ').replace(',', '')
        try:
            artist_name = str(artist_name)
        except ValueError:
            print('Artist name should be string')
            artist_name = ''
    while album_name == '':
        album_name = input('Album Name: ').replace(',', '')
        try:
            album_name = str(album_name)
        except ValueError:
            print('Album name should be string')
            album_name = ''
    while release_year == '':
        release_year = input('Release Year: ').replace(',', '')
        try:
            release_year = int(release_year)
        except ValueError:
            print('Release year should be integer')
            release_year = ''
        else:
            release_year = str(release_year)
    while genre == '':
        genre = input('Genre: ').replace(',', '')
        try:
            genre = str(genre)
        except ValueError:
            print('Genre should be string')
            album_name = ''
    while lenght == '':
        lenght = input('Lenght (mm:ss): ').replace(',', '')
        if re.match('[0-9]{1,3}:[0-6][0-9]', lenght):
            continue
        else:
            print('Bad format')
            lenght = ''


    album_data = [artist_name, album_name, release_year, genre, lenght]
    return album_data
    