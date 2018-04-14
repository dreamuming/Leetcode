from __future__ import print_function
import math

class Shape(object):
	def __init__(self):
		self.color = "red"
		self.sides = 0

	def calcArea(self):
		return 0


class Quadrilateral(Shape):
	def __init__(self, w, l, c):
		self.sides = 4
		self.width = w
		self.lenght = l
		self.color = c
	def calcArea(self):
		return self.lenght * self.width

class Square(Quadrilateral):
	def __init__(self, w, c):
		super(Square, self).__init__(w, w, c)

class Circle(Shape):
	def __init__(self, r, c):
		super(Circle, self).__init__()
		self.radius = r
		self.color = c

	def calcArea(self):
		return math.pi * (self.radius ** 2)

class Triangle(Shape):
	def __init__(self, s1, s2, s3, c):
		super(Triangle, self).__init__()
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.c = c


def printArea(s):
	print(s.calcArea());

sq1 = Square(5, "blue")
sq2 = Square(9, "green")

circle1 = Circle(10, "orange")
t1 = Triangle(2,3,4, "purple")

print("Square sizes:", sq1.width, "x", sq1.sides, sq1.color, 
	",", sq2.width, "x", sq2.sides, sq2.color)
print("Circle:", circle1.radius, circle1.color)

printArea(circle1)


		

