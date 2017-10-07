'''Sets the cover of all the mp3 files in the directory it is in.
The cover image must be in the directory and it's name must be "cover" and it's extension must be png or jpg.'''

import os
from mutagen.id3 import ID3, APIC

files = os.listdir('.')
mp3Files = [file for file in files if '.mp3' in file]

cover_ext = ''
if 'cover.png' in files:
    cover_ext = 'png'
elif 'cover.jpg' in files:
    cover_ext = 'jpg'
else:
    print('ERROR: Neither "cover.png" nor "cover.jpg" is found in the directory')
    exit()

cover = open('cover.' + cover_ext, 'rb').read()

for filename in mp3Files:

    file = ID3(filename)
    file.delall('APIC')
    file.add(APIC(3, 'image/' + cover_ext, 3, 'front cover', cover))
    file.save(v2_version=3)
