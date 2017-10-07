'''Sets the track number and title for all the mp3 files in the directory it is in.
The filename must begin with the track number split from the title with the string " - ".'''

import os
from mutagen.easyid3 import EasyID3 as ID3

files = os.listdir('.')
mp3Files = [file for file in files if '.mp3' in file]

for filename in mp3Files:

    tracknumber, title = '', ''

    try:
        tracknumber, title = filename[:-4].split(' - ', maxsplit=1)
    except ValueError:
        print('ERROR: The filenames must begin with the track number split from the title with the string " - ".')
        exit()


    file = ID3(filename)
    file['tracknumber'] = str(int(tracknumber))
    file['title'] = title
    file.save()
