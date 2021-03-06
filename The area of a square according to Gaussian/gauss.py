import math  #Импортируем библиотеку чтобы нам стала доступна функция abs.

class polygonal():
    """Класс для нахождения площади квадрата по Гауссу."""    
   
    def __init__(self, coordinates):
        """Инициализатор переменных."""
        self.coord = coordinates

    def calculation(self, coord):
        """Функция для вычисления."""
    
        #Создаем два пустых списка для дальнейших вычислений.
        x = []
        y = []
    
        #Создаем цикл который перебирает каждый элемент в переменной coordinates и добавляет их в два пустых списка.
        for i in self.coord:
            x.append(i[0])
            y.append(i[1])
      
        #Сами вычисления Гаусса. Конкретно эти ряды предназначены для вычисления 4 координат. Если координат больше необходимо будет добавлять по этой же логики в этот ряд.
        result_kx = x[0] * y[1] + x[1] * y[2] + x[2] * y[3] + x[3] * y[0]
        result_ky = x[1] * y[0] + x[2] * y[1] + x[3] * y[2] + x[0] * y[3]
    
        #Итоговый результат.
        result_xy = abs(result_kx - result_ky)/2
        return result_xy

#В данную переменную вбиваем координаты многоугольника. Пример: [(x1,y2), (x2,y2)].
coordinates = [(0,2),(2,2),(3,0),(1,1)]

#Создаем экземляр класса. И передаем ему в качестве аргумента наш список с вложеными кортежами.
obj = polygonal(coordinates)

#Выводим значение которое у нас получилось.
print(obj.calculation(coordinates))