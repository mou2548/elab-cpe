class Line():

    def __init__(self, x1, y1, x2, y2):
        self.slope = (y2-y1) / (x2-x1)
        self.y_intercept = y1 - self.slope * x1
        self.start_point = Point(x1, y1)
        self.end_point = Point(x2, y2)
    
    def contains(self, x, y):
        inRange = self.get_x1() <= x <= self.get_x2() and self.get_y1() <= y <= self.get_y2()
        return y == self.slope * x + self.y_intercept and inRange
    
    def get_distance(self):
        return ((self.get_y2()-self.get_y1()) ** 2 + (self.get_x2()-self.get_x1()) ** 2) ** 0.5
    
    def get_x1(self):
       return self.start_point.get_x()
    
    def get_y1(self):
       return self.start_point.get_y()
    
    def get_x2(self):
       return self.end_point.get_x()
    
    def get_y2(self):
       return self.end_point.get_y()
    
    def get_y(self, x):
        y = self.slope * x + self.y_intercept
        if self.contains(x, y):
           return y
        else:
           return -999.999

class Point:
    # Constuctor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_on_x_axis(self):
        if self.__y == 0: return True
        else: return False

    def is_on_y_axis(self):
        if self.__x == 0: return True
        else: return False

    def translate(self, dist_x, dist_y):
        self.__x = self.__x + dist_x
        self.__y = self.__y + dist_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))
y2 = float(input("Enter y2 : "))

line = Line(x1, y1, x2, y2)
print(f"value of x1 on this line is {line.get_x1():.3f}")
print(f"value of x2 on this line is {line.get_x2():.3f}")
print(f"value of y1 on this line is {line.get_y1():.3f}")
print(f"value of y2 on this line is {line.get_y2():.3f}")

print("==========")
print("Check x and y are on this line ?")
x_check = float(input("Enter x : "))
y_check = float(input("Enter y : "))
if line.contains(x_check, y_check):
    result_check = ""
else:
    result_check = "not "
print(f"x = {x_check:.3f} and y = {y_check:.3f} are {result_check}on this line")
print(f"Distance between startPoint and endPoint is {line.get_distance():.3f}")
print("==========")

print("Find value of y that gives( x , y ) on this line")
x_find = float(input("Enter x : "))
y_find = line.get_y(x_find)
print(f"value of y is {y_find:.3f}")
if y_find == -999.999:
    result_find = "is not "
else:
    result_find = ""
print(f"( x , y ) = ( {x_find:.3f} , {y_find:.3f} ) {result_find}on this line")
