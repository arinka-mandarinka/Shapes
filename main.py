import os

from figures import *
from prettytable import PrettyTable

shapes = []

def print_header(msg):
      os.system('cls')
      print(msg.upper() + '\n')

def print_table_figures(shapes):
    table = PrettyTable(['Номер', 'Название', 'Периметр', 'Площадь'])  
    data = []
    for i in range(len(shapes)):
        data.append(i + 1)
        data.append(shapes[i].name.capitalize())
        data.append(round(shapes[i].get_perimeter(), 2))
        data.append(round(shapes[i].get_area(), 2))

    while data:
        table.add_row(data[:4])
        data = data[4:]

    os.system('cls')
    print_header('фигуры отсортированные по площади')
    print(table)
    print()

def input_num(msg):
      while True:
            try:
                  num = int(input(msg))
            except:
                  print('Ошибка: введенно неверное значение! Попробуйте ещё раз...')
                  continue
            return num

def get_crds_pnt_str(crdnts, point):
      return 'Введите координату ' + crdnts + ' для точки ' + point + ': '

def input_count_shapes():
      print_header('программа для работы с фигурами')
      return input_num('Введите количество фигур: ')

def input_shapes(countShapes):
      for i in range(countShapes):
            print_header('выбор фигуры')
            print('1 - Треугольник\n' +
                  '2 - Круг\n' + 
                  '3 - Прямоугольный четырехугольник\n')
            numOfShape = input_num('Введите номер фигуры: ')
            shapes.append(input_crds_shape(numOfShape))

def input_crds_shape(numOfShape):
      match numOfShape:
            case 1:
                  print_header('заполнение треугольника')
                  shape = Triangle(
                        Point(input_num(get_crds_pnt_str('x', 'A')), input_num(get_crds_pnt_str('y', 'A'))),
                        Point(input_num(get_crds_pnt_str('x', 'B')), input_num(get_crds_pnt_str('y', 'B'))),
                        Point(input_num(get_crds_pnt_str('x', 'C')), input_num(get_crds_pnt_str('y', 'C')))
                  )
            case 2:
                  print_header('заполнение круга')
                  shape = Circle(
                        Point(input_num(get_crds_pnt_str('x', 'A')), input_num(get_crds_pnt_str('y', 'A'))),
                        Point(input_num(get_crds_pnt_str('x', 'B')), input_num(get_crds_pnt_str('y', 'B')))
                  )
            case 3:
                  print_header('заполнение прямоугольного четырехугольника')
                  shape = Quadrilateral(
                        Point(input_num(get_crds_pnt_str('x', 'A')), input_num(get_crds_pnt_str('y', 'A'))),
                        Point(input_num(get_crds_pnt_str('x', 'B')), input_num(get_crds_pnt_str('y', 'B'))),
                        Point(input_num(get_crds_pnt_str('x', 'C')), input_num(get_crds_pnt_str('y', 'C'))),
                        Point(input_num(get_crds_pnt_str('x', 'D')), input_num(get_crds_pnt_str('y', 'D')))
                  )
      return shape

if __name__ == '__main__':
      count = input_count_shapes()
      input_shapes(count)
      shapes.sort(key=lambda shape: shape.get_area())
      print_table_figures(shapes)


