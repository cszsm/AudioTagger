'''Renames all the mp3 files in the directory by the algorithm given in the 'renames' variable.'''

import os

files = os.listdir('.')
mp3Files = [file for file in files if '.mp3' in file]
flacFiles = [file for file in files if '.flac' in file]
audioFiles = mp3Files + flacFiles

# renames = [{
#     'old': file,
#     'new': file.replace('. ', ' - ')
# } for file in mp3Files]
renames = [{
    'old': file,
    'new': file[:2] + ' -' + file[2:]
} for file in audioFiles]

for file in renames:
    os.rename(file['old'], file['new'])
