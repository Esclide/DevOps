from hw16 import Navigator
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def getCoordinates(path):
    exif = Image.open(path)._getexif()

    if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)

        if 'GPSInfo' in exif:
            for key in exif['GPSInfo'].keys():
                name = GPSTAGS.get(key, key)
                exif['GPSInfo'][name] = exif['GPSInfo'].pop(key)
        else:
            return ("По данному фото невозможно определить координаты")


    info = exif['GPSInfo']


    for key in ['Latitude', 'Longitude']:
        if 'GPS' + key in info and 'GPS' + key + 'Ref' in info:
            e = info['GPS' + key]
            ref = info['GPS' + key + 'Ref']
            info[key] = (e[0][0] / e[0][1] +
                         e[1][0] / e[1][1] / 60 +
                         e[2][0] / e[2][1] / 3600
                         ) * (-1 if ref in ['S', 'W'] else 1)

        if 'Latitude' in info and 'Longitude' in info:
            return [info['Latitude'], info['Longitude']]




coordinates =  (getCoordinates('photo1.jpg'))
nav = Navigator()
nav.getAddrByCoordinates(coordinates[0], coordinates[1])