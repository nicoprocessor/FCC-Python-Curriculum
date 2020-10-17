class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.height + 2*self.width

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            out = ""
            for y in range(0, self.height):
                out += "*" * self.width + "\n"
            return out

    def get_amount_inside(self, arg_shape):
        return self.width // arg_shape.width * self.height // arg_shape.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return "Square(side={})".format(self.width)
