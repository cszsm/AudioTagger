'''Sets the track number and title for all the mp3 files in the directory it is in.
The filename must begin with the track number split from the title with the string " - ".'''

import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.id3 import TYER, TALB, TRCK, TIT2


def getTrackAndTitle(filename):
    try:
        tracknumber, title = filename.split(' - ', maxsplit=1)
        return str(int(tracknumber)), title
    except ValueError:
        print(
            'ERROR: The filenames must begin with the track number split from the title with the string " - ".'
        )
        exit()


def getYearAndAlbum(dirname):
    try:
        year, album = dirName.split(' - ', maxsplit=1)
        return year, album
    except ValueError:
        print(
            'ERROR: The parent directory must begin with the year split from the album name with the string " - ".'
        )
        exit()


def setTags(file, tags):
    file['date'] = tags['year']
    file['album'] = tags['album']
    file['tracknumber'] = tags['tracknumber']
    file['title'] = tags['title']
    file.save()


tags = {}

dirPath = os.getcwd()
parentDirPath, dirName = os.path.split(dirPath)
parentDirName = os.path.split(parentDirPath)[1]
tags['year'], tags['album'] = getYearAndAlbum(dirName)

files = os.listdir('.')
mp3Files = [file[:-4] for file in files if '.mp3' in file]
flacFiles = [file[:-5] for file in files if '.flac' in file]

# for filename in mp3Files:
#     file = EasyID3(filename + '.mp3')
#     tags['tracknumber'], tags['title'] = getTrackAndTitle(filename)
#     setTags(file, tags)

# for filename in flacFiles:
#     file = FLAC(filename + '.flac')
#     tags['tracknumber'], tags['title'] = getTrackAndTitle(filename)
#     setTags(file, tags)

for filename in mp3Files:
    file = ID3(filename + '.mp3')

    tracknumber, title = getTrackAndTitle(filename)

    file.delall('TYER')
    file.add(TYER(text=tags['year']))

    file.delall('TALB')
    file.add(TALB(text=tags['album']))

    file.delall('TRCK')
    file.add(TRCK(text=tracknumber))

    file.delall('TIT2')
    file.add(TIT2(text=title))

    file.save()
