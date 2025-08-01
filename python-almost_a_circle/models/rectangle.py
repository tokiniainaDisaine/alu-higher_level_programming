#!/usr/bin/python3
""" 
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
Proin finibus pharetra lorem, accumsan sagittis felis pretium
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        return self.width * self.height

    def display(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Proin iaculis tellus a felis sodales pulvinar. Mauris tempor
        placerat sem et ultrices. Donec ut dapibus turpis, a feugiat
        Proin finibus pharetra lorem, accumsan sagittis felis pretium
        """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
