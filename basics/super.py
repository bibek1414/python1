    # class Rectange:
    #     def area(self,legth,width):
    #         return legth*width
        
    # class Square(Rectange):
    #     def area(self,side_length):
    #         return super().area(side_length,side_length)

    # square=Square()
    # print(square.area(4))


    # class Rectange:
    #     def area(self,legth,width):
    #         return legth*width
        
    # class Square(Rectange):
    #     def __init__(self,side_length):
    #         sqr= super().area(side_length,side_length)
    #         print(f"The square of the number is {sqr}")

    # square=Square(4)

    # area is parent class all set in parent class length breadth height pi value def square_area
    # child class is square
    #  rectangle 
    # circle
    #  triangle
# class Area:
#     pi = 3.14159

#     def square_area(self, side):
#         return side * side

#     def rectangle_area(self, length, width):
#         return length * width

#     def circle_area(self, radius):
#         return self.pi * radius * radius

#     def triangle_area(self, base, height):
#         return 0.5 * base * height


# class Square(Area):
#     def __init__(self, side_length):
#         result = self.square_area(side_length)
#         print(f"The area of the square is {result}")


# class Rectangle(Area):
#     def __init__(self, length, width):
#         result = self.rectangle_area(length, width)
#         print(f"The area of the rectangle is {result}")


# class Circle(Area):
#     def __init__(self, radius):
#         result = self.circle_area(radius)
#         print(f"The area of the circle is {result}")


# class Triangle(Area):
#     def __init__(self, base, height):
#         result = self.triangle_area(base, height)
#         print(f"The area of the triangle is {result}")


# square = Square(4)
# rectangle = Rectangle(5, 3)
# circle = Circle(7)
# triangle = Triangle(6, 4)
class Area:
    pi = 3.14159

    def square_area(self, side):
        return side * side

    def rectangle_area(self, length, width):
        return length * width

    def circle_area(self, radius):
        return self.pi * radius * radius

    def triangle_area(self, base, height):
        return 0.5 * base * height


class Square(Area):
    def __init__(self, side_length):
        result = super().square_area(side_length)
        print(f"The area of the square is {result}")


class Rectangle(Area):
    def __init__(self, length, width):
        result = super().rectangle_area(length, width)
        print(f"The area of the rectangle is {result}")


class Circle(Area):
    def __init__(self, radius):
        result = super().circle_area(radius)
        print(f"The area of the circle is {result}")


class Triangle(Area):
    def __init__(self, base, height):
        result = super().triangle_area(base, height)
        print(f"The area of the triangle is {result}")


square = Square(4)
rectangle = Rectangle(5, 3)
circle = Circle(7)
triangle = Triangle(6, 4)





