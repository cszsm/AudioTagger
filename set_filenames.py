'''Sets the filenames by the files' titles'''

import os
from mutagen.easyid3 import EasyID3 as ID3

files = os.listdir('.')
mp3Files = [file for file in files if '.mp3' in file]

for filename in mp3Files:

    file = ID3(filename)

    tracknumber = filename[:2]
    title = file.get('title')[0]

    os.rename(filename, tracknumber + ' - ' + title + '.mp3')
