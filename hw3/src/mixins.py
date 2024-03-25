import os

import numpy as np

from matrix import MyMatrix


class SaveMixinMatrix:

    def save(self, save_dir, filename):
        filepath = os.path.join(save_dir, filename)
        with open(filepath, 'w+') as f:
            f.write(str(self))


class StringMixinMatrix:

    def __str__(self):
        return '\n'.join(['\t'.join([str(x) for x in row]) for row in self.mx]) + '\n'


class HashMixinMatrix:
    def __eq__(self, other):
        # для проверки на неравенство - достаточно, а равенство мы не проверяем
        return self.mx[0][0] == other.mx[0][0]

    def __hash__(self):
        return int(sum(self.mx[0]))


class CoolerMatrix(MyMatrix, SaveMixinMatrix, StringMixinMatrix, HashMixinMatrix):
    _HANDLED_TYPES = (np.ndarray,)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (type(self),)):
                return NotImplemented

        inputs = tuple(x._mx if isinstance(x, type(self)) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x._mx if isinstance(x, type(self)) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
