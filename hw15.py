import ipaddress


class Router:
    listIpInterfaces = []
    # [[gateway1:route1], [gateway1:route2]]
    listIpRoutes = []

    def addIpAddress(self, ipInterface):
        try:
            if ipInterface not in self.listIpInterfaces:
                self.listIpInterfaces.append(ipaddress.ip_interface(ipInterface))
                return 'Адрес успешно добавлен'
            return 'Данный адрес уже присутствует'
        except ValueError:
            return 'Введите корректный ip-адрес интерфейса'

    # Проверяем, присутствует ли маршрут до сети
    def ifHaveRoute(self, ipGateway):
        for routes in self.listIpRoutes:
            if ipGateway in routes[1]:
                return True
        return False

    # Проверяем, относится ли ip к одной из сетей в listIpAddresses
    def ifIpInListNetworks(self, ipAddress):
        for address in self.listIpInterfaces:
            if ipAddress in address.network:
                return True
        return False

    def addIpRoute(self, ipRouteGateway, networkAddress):
        try:
            ipRouteGateway = ipaddress.ip_address(ipRouteGateway)
            networkAddress = ipaddress.ip_network(networkAddress)
        except ValueError:
            return 'Введите корректный ip-адрес'

        if (not self.ifIpInListNetworks(ipRouteGateway)) and (not self.ifHaveRoute(ipRouteGateway)):
            return 'Маршрут до шлюза отсутствует'
        if [ipRouteGateway, networkAddress] in self.listIpRoutes:
            return 'Данный маршрут уже присутствует в таблице'
        self.listIpRoutes.append([ipRouteGateway, networkAddress])
        return 'Маршрут успешно добавлен'

    def delIpAddress(self, ipAddress):
        try:
            ipInterface = ipaddress.ip_interface(ipAddress)
        except ValueError:
            return 'Введите корректный ip-адрес интерфейса'
        if ipInterface in self.listIpInterfaces:
            self.delIpRoute(ipInterface.network)
            self.listIpInterfaces.remove(ipInterface)
            return 'Удавление выполнено успешно'
        return 'Значение адреса отсутствует'

    # Удаляем сам маршрут и дочерние маршруты
    def delIpRoute(self, network):
        try:
            network = ipaddress.ip_network(network)
        except ValueError:
            return 'Введите корректный ip-адрес интерфейса'

        counter = 0
        for route in self.listIpRoutes:
            if route[1] == network:
                self.listIpRoutes.remove(route)
                self.delIpRoute(route[1])
                counter = 1
            if route[0] in network:
                self.delIpRoute(route[1])
        if counter == 1: return "Удаление выполнено успешно"
        return "Удаление не выполнено. Проверьте введенные данные"

    def getIpAddresses(self):
        strAddresses = ''
        for address in self.listIpInterfaces:
            strAddresses += str(address) + '; '

        return strAddresses

    def getIpRoutes(self):
        strRoutes = ''
        for route in self.listIpRoutes:
            strRoutes += 'через ' + str(route[0]) + ' маршрут до ' + str(route[1]) + '\n'

        return strRoutes[0:]

    def printInfo(self):
        print("ip адреса на интерфейсах роутера:\n" + self.getIpAddresses())
        print("Маршруты к подключенным сетям:\n" + self.getIpRoutes())

    def printIpAddresses(self):
        print("ip адреса на интерфейсах роутера:\n" + self.getIpAddresses())

    def printIpRoutes(self):
        print("Маршруты к подключенным сетям:\n" + self.getIpRoutes())


router = Router()
print(router.addIpAddress('192.168.5.14/24'))
print(router.addIpAddress('193.168.5.14/24'))

print(router.addIpRoute('192.168.5.1', '172.16.0.0/16'))
print(router.addIpRoute('192.168.8.1', '172.24.0.0/16'))
print(router.addIpRoute('172.16.8.1', '172.24.0.0/16'))

print(router.addIpRoute('193.168.5.1', '173.16.0.0/16'))
print(router.addIpRoute('193.168.8.1', '173.24.0.0/16'))
print(router.addIpRoute('173.16.8.1', '173.24.0.0/16'))

print()
router.printInfo()

print(router.delIpAddress('192.168.5.14/24'))

print()
router.printInfo()
print()
