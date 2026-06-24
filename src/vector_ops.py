import numpy as np

def add_vectors(a, b):
    return a + b

def dot_product(a, b):
    return np.dot(a, b)

def vector_norm(a):
    return np.linalg.norm(a)

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("a + b =", add_vectors(a, b))
    print("a · b =", dot_product(a, b))
    print("|a| =", vector_norm(a))
