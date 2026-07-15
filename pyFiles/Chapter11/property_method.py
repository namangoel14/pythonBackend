class Employee:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

e = Employee("Naman")
print(e.name)


class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

# @.getter() method 

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

# @.setter() method
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
       if new_height > 0:
            self._height = new_height
       else:
           print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width is successfully deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height is successfully deleted")

rectangle = Rectangle(9, 10)

rectangle.width = 3
rectangle.height = 4

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
