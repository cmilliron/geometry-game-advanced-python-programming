import random

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
                and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
        self.rec_area = self.area()

    def area(self):
        change_in_x = abs(self.upright.x - self.lowleft.x)
        change_in_y = abs(self.upright.y - self.lowleft.y)
        return change_in_y * change_in_x

point_x = Point(random.randint(0, 9), random.randint(0, 9))
point_y = Point(random.randint(0, 9), random.randint(0, 9))

rec_x = Rectangle(point_x, point_y)

text_x = int(input("Enter x component: "))
test_y = int(input("Enter y component: "))

test = Point(text_x, test_y)

print(rec_x)
print(test.falls_in_rectangle(rec_x))
