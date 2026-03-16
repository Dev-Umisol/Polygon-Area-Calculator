import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width): # Setter
        self.width = width
    
    def set_height(self, height): # Setter
        self.height = height
    
    def get_area(self): # Getter
        area = self.width * self.height
        return area
    
    def get_perimeter(self): # Getter
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    def get_diagonal(self): # Getter
        diagonal = math.sqrt(pow(self.width, 2) + pow(self.height, 2))
        return diagonal

    def get_picture(self):
        picture = ""
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for shape in range(self.height):
                picture += "*" * self.width + "\n"
            return picture
    
    def get_amount_inside(self, shape):
        shape_width = self.width // shape.width
        shape_height = self.height // shape.height
        shape = shape_width * shape_height
        
        return shape
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length)
    
    def set_width(self, width):
        pass
    
    def set_height(self, height):
        pass
    
    def set_side(self, side):
        pass