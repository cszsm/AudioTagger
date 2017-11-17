'''Sets the filenames by the files' titles'''

import os
from mutagen.easyid3 import EasyID3 as ID3
from mutagen.flac import FLAC

files = os.listdir('.')
mp3Files = [file for file in files if '.mp3' in file.lower()]
flacFiles = [file for file in files if '.flac' in file.lower()]

for filename in mp3Files:
    file = ID3(filename)

    tracknumber = file.get('tracknumber')[0]
    title = file.get('title')[0]

    os.rename(filename, tracknumber + ' - ' + title + '.mp3')

for filename in flacFiles:
    file = FLAC(filename)

    tracknumber = file.get('tracknumber')[0]
    title = file.get('title')[0]

    os.rename(filename, tracknumber + ' - ' + title + '.flac')
