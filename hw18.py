from PIL import Image
import os

def resizeByWidth(path, width, saveName):
    img = Image.open(path)
    print("Исходные размеры: {}х{}".format(img.size[0], img.size[1]))
    widthPercent = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(widthPercent)))
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save('{}.jpg'.format(saveName))
    print("Результирующие размеры: {}х{}".format(img.size[0], img.size[1]))

def resizeByHeight(path, height, saveName):
    img = Image.open(path)
    print("Исходные размеры: {}х{}".format(img.size[0], img.size[1]))
    heightPercent = (height / float(img.size[1]))
    width = int((float(img.size[0]) * float(heightPercent)))
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save('{}.jpg'.format(saveName))
    print("Результирующие размеры: {}х{}".format(img.size[0], img.size[1]))

def resize(path, height, width, saveName):
    img = Image.open(path)
    print("Исходные размеры: {}х{}".format(img.size[0], img.size[1]))
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save('{}.jpg'.format(saveName))
    print("Результирующие размеры: {}х{}".format(img.size[0], img.size[1]))


path = 'photo.jpg'
resizeByHeight(path, 100, 'photo_1')
print()
resizeByWidth(path, 100, 'photo_2')
print()
resize(path, 100, 100, 'photo_3')
