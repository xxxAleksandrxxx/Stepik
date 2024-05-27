# class Address:
#     def __init__(self, city=None, street=None, house=None, flat=None):
#         self.city = city
#         self.street = street
#         self.house = house
#         self.flat = flat

# a = Address(
#     city = "Moscow",
#     street = "3-ya ulitsa stroiteley",
#     house = "25",
#     flat = "12"
# )


# import sys
# print(sys.getsizeof([1, 2, 3]))


# from pympler.asizeof import asizeof

# print(None, "-", asizeof(None), "byte")
# print(3, "-", asizeof(3), "byte")
# print(3.14, "-", asizeof(3.14), "byte")
# print("", "-", asizeof(""), "byte")
# print(list(), "-", asizeof(list()), "byte")
# print(tuple(), "-", asizeof(tuple()), "byte")
# print(set(), "-", asizeof(set()), "byte")
# print(dict(), "-", asizeof(dict()), "byte")


# from pympler.asizeof import asizeof

# class Rect():
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2

# print(asizeof(Rect(0, 0, 0, 0)))


# from pympler.asizeof import asizeof

# class Rect():
#     __slots__ = ("x1", "x2", "y1", "y2")
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.x2 = x2
#         self.y1 = y1
#         self.y2 = y2

# print(asizeof(Rect(0, 0, 0, 0)))


# from pympler.asizeof import asizeof

# rect = (0, 0, 0, 0)
# print(asizeof(rect))


# from pympler.asizeof import asizeof
# from collections import namedtuple

# Rect = namedtuple('Rec', 'x1 x2 x3 x4')
# print(asizeof(Rect(0, 0, 0, 0)))


# import struct
# from pympler.asizeof import asizeof
# data = struct.pack(' llll', 0, 0, 0, 0)
# print("data", asizeof(data))

# x1, y1, x2, y2 = struct.unpack('llll', data)
# print("x1", asizeof(x1))
# print("x2", asizeof(x2))
# print("y1", asizeof(y1))
# print("y2", asizeof(y2))


# import struct

# # Создаем 1000 точек (x, y) типа float
# points = [(i * 0.1, i * 0.2) for i in range(1000)]

# # Упаковываем точки в байтовый массив
# # 'f' означает "float" (4 байта на число)
# packed_data = bytearray(struct.pack(f'{len(points)}f{len(points)}f', *[coord for point in points for coord in point]))

# # Создаем memoryview для байтового массива
# view = memoryview(packed_data)

# # Получаем 500-ю точку
# point_index = 500
# point_size = struct.calcsize('ff') # размер одной точки в байтах
# point_offset = point_index * point_size
# x, y = struct.unpack_from('ff', view[point_offset:point_offset + point_size])

# print(f"Точка {point_index}: ({x}, {y})")

# # Изменяем координаты 500-й точки
# new_x = 100.0
# new_y = 200.0
# struct.pack_into('ff', view, point_offset, new_x, new_y)

# # Распаковываем измененную точку
# x, y = struct.unpack_from('ff', view[point_offset:point_offset + point_size])

# print(f"Измененная точка {point_index}: ({x}, {y})")


# a = "abcdefghijklmnopqrstuvwxyz"
# b = "abcdefghijklmnopqrstuvwxyz"
# print("a", id(a))
# print("b", id(b))

# a = "x"*10
# b = "x"*10
# print("a", id(a))
# print("b", id(b))


# from io import StringIO

# def create_html_list(items):
#   """Создаёт HTML список из элементов."""
#   html = StringIO()
#   html.write("<ul>\n")
#   for item in items:
#     html.write(f"  <li>{item}</li>\n")
#   html.write("</ul>")
#   return html.getvalue()

# items = ["Яблоки", "Груши", "Бананы"]
# print(create_html_list(items))


# import csv
# from io import StringIO

# output = StringIO()
# writer = csv.writer(output)
# writer.writerow(["Имя", "Возраст"])
# writer.writerow(["Иван", 30])

# # output содержит данные в формате CSV
# print(output.getvalue())


