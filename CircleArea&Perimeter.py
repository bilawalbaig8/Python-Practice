''' Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle  '''


# # line code
# radius = 5
#
# area = 3.14 * (radius ** 2)
# perimeter = 2 * 3.14 * radius
#
# print("Area of the circle:", area)
# print("Perimeter of the circle:", perimeter)

# # Function
# def CircleCal(radius):
#
#     area = 3.14 * (radius ** 2)
#
#     perimeter = 2 * 3.14 * radius
#
#     return area, perimeter
#
# area, perimeter = CircleCal(5)
#
#
# print("Area : ", area)
# print("Perimeter : ", perimeter)

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area

    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter

circle = Circle(5)

area = circle.area()
print(area)

perimeter = circle.perimeter()
print(perimeter)
