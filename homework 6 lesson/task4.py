import json
from datetime import timedelta


def open_file():
    with open('acdc.json', 'r+') as file:
        data = json.load(file)

        tracks = data['album']['tracks']['track']
        total = sum(int(track['duration']) for track in tracks)
        print(timedelta(seconds=total))


open_file()

