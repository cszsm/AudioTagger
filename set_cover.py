'''Sets the cover of all the mp3 files in the directory it is in.
The cover image must be in the directory and it's name must be "cover" and it's extension must be png or jpg.'''

import os
from mutagen.id3 import ID3, APIC
from mutagen.flac import FLAC

files = os.listdir('.')
mp3Files = [file for file in files if '.mp3' in file.lower()]
flacFiles = [file for file in files if '.flac' in file.lower()]

cover_ext = ''
if 'cover.png' in files:
    cover_ext = 'png'
elif 'cover.jpg' in files:
    cover_ext = 'jpg'
else:
    print(
        'Cover is not set. Neither "cover.png" nor "cover.jpg" is found in the directory'
    )
    exit()

# artist_ext = ''
# if 'artist.png' in files:
#     artist_ext = 'png'
# elif 'artist.jpg' in files:
#     artist_ext = 'jpg'
# else:
#     print(
#         'Artist image is not set. Neither "artist.png" nor "artist.jpg" is found in the directory'
#     )
#     exit()

cover = open('cover.' + cover_ext, 'rb').read()
# artist = open('artist.' + artist_ext, 'rb').read()

for filename in mp3Files:
    file = ID3(filename)

    file.delall('APIC')
    file.add(APIC(3, 'image/' + cover_ext, 3, '$03', cover))
    # file.add(APIC(3, 'image/' + artist_ext, 3, '$08', cover))

    file.save(v2_version=3)

# for filename in flacFiles:
#     file = FLAC(filename)

#     file.clear_pictures()
#     file.add_picture(cover)

#     file.save()
