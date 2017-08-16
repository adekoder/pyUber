import tablib

pyMap = [
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_']
]

class PyUber():
    
    car = 'C'
    passenger = 'P'
    destination = 'D'

    def __init__(self,car_cord):
        self.car_cord = car_cord
        self.car_cord_x = self.car_cord[0]
        self.car_cord_y = self.car_cord[1]
        self.pymap = pyMap 
        self.insertNewPos(self.car_cord_x, self.car_cord_y, PyUber.car)
        print('Initial start')
        self.printPosition()

    def pickUpPassenger(self, position):
        self.px = position[0]
        self.py = position[1]
        self.insertNewPos(self.px, self.py, PyUber.passenger)
        self.__drive(self.px, self.py) 
        print('dropped passenger... ')
    
    def dropPassenger(self, position):
        self.px = position[0]
        self.py = position[1]
        self.insertNewPos(self.px, self.py, PyUber.destination)
        self.__drive(self.px, self.py)
        print('dropped passenger... ')
    
    def __drive(self, px, py):
        while (self.car_cord_x != px or self.car_cord_y != py):
            prev_x = self.car_cord_x
            prev_y = self.car_cord_y
            self.get_x_cord(px)
            self.get_y_cord(py)
            self.clearPos(prev_x,prev_y)    
            self.insertNewPos(self.car_cord_x, self.car_cord_y, PyUber.car)
            self.printPosition()

                    

    def insertNewPos(self, x_cord, y_cord , data):
        self.pymap[x_cord][y_cord] = data

    def clearPos(self, x_cord, y_cord):
        self.pymap[x_cord][y_cord] = '_'

    def get_x_cord(self, px):
        
        if self.car_cord_x > px:
                self.car_cord_x -= 1
        elif self.car_cord_x < px:
            self.car_cord_x += 1

        return self.car_cord_x

    def get_y_cord(self, py):
            
        if self.car_cord_y > py:
                self.car_cord_y -= 1
        elif self.car_cord_y < py:
            self.car_cord_y += 1
            
        return self.car_cord_y
        
          
    def  printPosition(self):
        data = tablib.Dataset()
        for row in self.pymap:
            data.append(row)
        print('-' * 30)
        print(data)

if __name__ == '__main__':   

    car = PyUber((3, 1))
    car.pickUpPassenger((7,7))
    car.dropPassenger((3,7))