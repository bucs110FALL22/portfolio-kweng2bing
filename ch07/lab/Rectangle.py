class Rectangle:
    def __init__(self, x, y, height, width):
        change= [x, y, height, width]
        for i in range(len(change)):
            j= change[i]
            if j < 0:
                change[i]=0
        self.x = change[0]
        self.y = change[1]
        self.height = change[2]
        self.width = change[3]
        print(change)

    def __str__(self):
        resultStr =f"(x:{self.x}, y:{self.y}, height:{self.height}, width:{self.width})"
        return resultStr
