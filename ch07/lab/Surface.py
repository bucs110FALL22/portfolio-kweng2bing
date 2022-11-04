from Rectangle import Rectangle
class Surface:
    def __init__(self, filename, x,y,h, w):
        # The inputs are placed into a function and  either returns something from the method Rectangle or gives the filename
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        # Returns the rectangle
        return self.rect

