class MyMatrix:
    def __init__(self, data: list[list]):
        self.validate(data)
        self._mx = data

    @property
    def mx(self):
        return self._mx

    @mx.setter
    def mx(self, data):
        self.validate(data)
        self._mx = data

    @mx.getter
    def mx(self):
        return self._mx

    def __add__(self, other):
        if len(self._mx) == len(other.mx):
            return self.__class__(
                [[self._mx[i][j] + other.mx[i][j] for j in range(len(self.mx[i]))] for i in range(len(self.mx))])
        else:
            raise ValueError('Matrix dimensions do not match')

    def __mul__(self, other):
        return self.__class__(
            [[self._mx[i][j] * other.mx[i][j] for j in range(len(self.mx[i]))] for i in range(len(self.mx))])

    def __matmul__(self, other):
        if len(self._mx[0]) == len(other.mx):
            return self.__class__([[sum(self._mx[i][j] * other.mx[j][k] for j in range(len(self.mx[i]))) for k in
                                    range(len(other.mx[0]))] for i in range(len(self.mx))])
        else:
            raise ValueError('Matrix dimensions do not match')

    @staticmethod
    def validate(data):
        if len(data) == 0:
            raise ValueError('Empty matrix')
        for row in data:
            if len(row) != len(data[0]):
                raise ValueError('Invalid matrix')
