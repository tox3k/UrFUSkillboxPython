from datetime import date
class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        if not isinstance(value, tuple):
            raise TypeError('Coordinates must be represented as tuple (pos_x: int, pos_y: int)')

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('Coordinates\' values must be integer!')
        self._coordinates = (value[0], value[1])

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, int):
            raise TypeError('Speed value must be integer!')
        if value < 0:
            raise ValueError('Speed can\'t be negative!')
        self._speed = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError('Brand name must be a string!')
        self._brand = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError('Year must be integer!')

        if value < 0:
            raise ValueError('Year can\'t be negative!')

        if value > date.today().year:
            raise ValueError('Year can\'t be higher than current!')

        self._year = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError('Number must be integer!')

        if value < 0:
            raise ValueError('Number can\'t be negative!')

        self._number = value





    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''

        return (f'Coordinates (X, Y): {self.coordinates},'
                f' Speed: {self.speed},'
                f' Brand: {self.brand},'
                f' Year: {self.year},'
                f'Number: {self.number}')



    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''

        if (pos_x <= self.coordinates[0] <= pos_x + width) and (pos_y <= self.coordinates[1] <= pos_y + length):
            return True

        return False


class Passenger:

    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if not isinstance(passengers_capacity, int):
            raise TypeError('Passengers capacity must be integer value!')

        if passengers_capacity < 0:
            raise ValueError('Passengers capacity can\'t be negative!')

        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if not isinstance(number_of_passengers, int):
            raise TypeError('Number of passengers capacity must be integer value!')

        if number_of_passengers < 0:
            raise ValueError('Passengers capacity can\'t be negative!')

        if number_of_passengers > self.passengers_capacity:
            raise ValueError('Number of passengers can\'t be higher than passengers capacity!')

        self._number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self, carrying):
        self.carrying = carrying
    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, str) or carrying is not None:
            raise TypeError('Carrying must be string value!')
        self._carrying



class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('Height must be integer value!')

        if value < 0:
            raise ValueError('Height can\'t be negative!')
        self._height = value


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if not isinstance(value, str):
            raise TypeError('Port name must be string value!')
        self._port = value


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        super(Auto, self).__init__(coordinates, speed, brand, year, number)
        super(Passenger, self).__init__(passengers_capacity, number_of_passengers)

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        super(Auto, self).__init__(coordinates, speed, brand, year, number)
        super(Cargo, self).__init__(carrying)

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        super(Ship, self).__init__(coordinates, speed, brand, year, number, port)
        super(Passenger, self).__init__(passengers_capacity, number_of_passengers)

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        super(Ship, self).__init__(coordinates, speed, brand, year, number, port)
        super(Cargo, self).__init__(carrying)

class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        super(Plane, self).__init__(coordinates, speed, brand, year, number, height)
        super(Cargo, self).__init__(carrying)

class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        super(Plane, self).__init__(coordinates, speed, brand, year, number, height)
        super(Passenger).__init__(passengers_capacity, number_of_passengers)

class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port):
        super(Plane, self).__init__(coordinates, speed, brand, year, number, height)
        self.port = port
