from array import array
import math


class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property  # make x readonly.
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):  # make vector iterable
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __complex__(self):
        img = self.__x
        real = self.__y
        return complex(img, real)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<r:{}, thera:{}>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __hash__(self):  # std suggest use ^ to mix hashes for components
        return hash(self.x) ^ hash(self.y)


class ShortVector2d(Vector2d):
    typecode = 'h'

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, map(lambda x: int(x), self))))

