import numpy as np

from mixins import CoolerMatrix


def perform_matrix_operations():
    np.random.seed(0)
    a = np.random.randint(0, 10, (10, 10))
    b = np.random.randint(0, 10, (10, 10))

    c = CoolerMatrix(a) * CoolerMatrix(b)
    c.save(r'hw3/artifacts/31/', 'matrix_mul.txt')

    c = CoolerMatrix(a) + CoolerMatrix(b)
    c.save(r'hw3/artifacts/31/', 'matrix_add.txt')

    c = CoolerMatrix(a) @ CoolerMatrix(b)
    c.save(r'hw3/artifacts/31/', 'matrix_matmul.txt')

    np.random.seed(None)


def find_valid_matrices():
    A = CoolerMatrix(np.random.randint(0, 10, (10, 10)))
    B = CoolerMatrix(np.random.randint(0, 10, (10, 10)))
    C = CoolerMatrix(np.random.randint(0, 10, (10, 10)))
    D = CoolerMatrix(np.random.randint(0, 10, (10, 10)))

    while not ((hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D)):
        A = CoolerMatrix(np.random.randint(0, 10, (10, 10)))
        B = CoolerMatrix(np.random.randint(0, 10, (10, 10)))
        C = CoolerMatrix(np.random.randint(0, 10, (10, 10)))
        D = B

    A.save(r'hw3/artifacts/33/', 'A.txt')
    B.save(r'hw3/artifacts/33/', 'B.txt')
    C.save(r'hw3/artifacts/33/', 'C.txt')
    D.save(r'hw3/artifacts/33/', 'D.txt')
    (A @ B).save(r'hw3/artifacts/33/', 'AB.txt')
    (C @ D).save(r'hw3/artifacts/33/', 'CD.txt')
    with open(r'hw3/artifacts/33/hash.txt', 'w+') as f:
        f.write(str(hash(A @ B)) + '\n')
        f.write(str(hash(C @ D)))


if __name__ == '__main__':
    perform_matrix_operations()
    find_valid_matrices()
