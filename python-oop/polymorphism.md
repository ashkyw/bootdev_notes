Basic example of using polymorphism to check if boxes are overlapping based on cartesian coords.

class Rectangle:
    def overlaps(self, rect):
        if (
            self.get_left_x() <= rect.get_right_x() and 
            self.get_right_x() >= rect.get_left_x() and 
            self.get_top_y() >= rect.get_bottom_y() and 
            self.get_bottom_y() <= rect.get_top_y()
            ):
                return True
        return False

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
