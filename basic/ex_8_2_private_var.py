import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius # private 멤버변수 선언 → 접두사로 __ 붙임
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    def get_radius(self):
        return self.__radius
    
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print("원의 반지름: ", circle.get_radius())
print()

print("# __radius에 접근합니다.")
print(circle.__radius)
# Traceback (most recent call last):
#   File "C:\Users\USER\Desktop\hancom\python\ex_8_2_private_var.py", line 20, in <module>
#     print(circle.__radius)
#           ^^^^^^^^^^^^^^^
# AttributeError: 'Circle' object has no attribute '__radius'. Did you mean: 'get_radius'?