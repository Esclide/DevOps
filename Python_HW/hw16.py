from opencage.geocoder import OpenCageGeocode
import requests


class Navigator:
    from opencage.geocoder import OpenCageGeocode
    import requests

    def printAddrFromFile(self, path):
        try:
            f = open(path, 'r')
        except FileNotFoundError:
            print("Файл с данным названием не найден")
            return
        lines = f.readlines()
        f.close()
        try:
            for line in lines:
                x, y = line.split(' ')[0].rstrip('\'').replace(',', '.'), line.split(' ')[1].rstrip('\'\n').replace(',',
                                                                                                                '.')
        except IndexError:
            print("В данном файле отсутствуют координаты")
            return
        for line in lines:
            self.printAddrByCoordinates(x, y)

    def printAddrByCoordinates(self, x, y):
        apiKey = "c1d69c5a2f3c4266bc4297d5d8cb64fd"
        geocoder = OpenCageGeocode(apiKey)
        try:
            results = geocoder.reverse_geocode(x, y)
        except Exception:
            print("Неверный формат координат")
            return
        print("Input data: " + str(x) + '; ' + str(y))
        if results == []:
            print("По данным координатам ничего не найдено")
            print()
            return
        print('Output data:')
        print('Location: '+str(self.translateYandex(results[0]['formatted']))[2:-2])
        print("GoogleMaps URL:", "https://www.google.com/maps/search/?api=1&query={},{}".format(x,y))
        print()


    def translateYandex(self, text):
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
        key = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961.08d0c5ada49017ed764c042723895ffab867be7a'
        text = text
        lang = 'en-ru'
        r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
        return r.text[r.text.find('['):-1]

if __name__ == '__main__':
    nav = Navigator()
    nav.printAddrFromFile('Coordinates.txt')
    nav.printAddrFromFile('HomeworkGit')

