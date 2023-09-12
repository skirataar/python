class Shape:
    def __init__(self,a,b,constant):
        print(a*b*constant)


class triangle(Shape):
    def __init__(self,b,h):
        super().__init__(b,h,0.5)
class circle(Shape):
    def __init__(self,r):
        super().__init__(r,r,3.1415)
class rect(Shape):
    def __init__(self,b,h):
        super().__init__(b,h,1)
print("Area of Triangle")
triangle(20,10)
print("Area of Circle")
circle(5)
print("Area of Rectangle")
rect(4,5)
