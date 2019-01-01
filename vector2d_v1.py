from array import array
import reprlib
import numbers
import math

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return(tuple(self) == tuple(other))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indicies must be integers'
            raise TypeError(msg.format(cls=cls))

    # def __format__(self, fmt_spec=''):
    #     if fmt_spec.endswith('p'):
    #         fmt_spec = fmt_spec[:-1]
    #         coords = (abs(self), self.angle())
    #         outer_fmt = '<{}, {}>'
    #     else:
    #         coords = self
    #         outer_fmt = '({}, {})'
    #     components = (format(c, fmt_spec) for c in self)
    #     return '({}, {})'.format(*components)

    # def __hash__(self):
    #     return hash(self.x) ^ hash(self.y)

    # def angle(self):
    #     return math.atan2(self.y, self.x)

    @classmethod
    def frombytecode(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

