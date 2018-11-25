import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    result = np.arange(n**2).reshape(n,n)
    return result


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        result = np.zeros(shape, dtype)
    elif type == 1:
        result = np.ones(shape, dtype)
    elif type == 99:
        result = np.empty(shape, dtype)
    return result


def change_shape_of_ndarray(X, n_row):
    if n_row == 1:
        result = X.flatten()
    else:
        result = X.reshape(n_row,-1)
    return result


def concat_ndarray(X_1, X_2, axis):
    if len(X_1.shape) == 1 or len(X_2.shape) == 1:
        X_1 = X_1.reshape(1,-1)
        X_2 = X_2.reshape(1,-1)

    if axis == 0:
        if X_1.shape[1] != X_2.shape[1]:
            return False
    elif axis == 1:
        if X_1.shape[0] != X_2.shape[0]:
            return False

    result = np.concatenate((X_1,X_2), axis)
    return result


def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 0:
        mean = X.mean(axis, dtype=dtype).reshape(1,-1)
        std = X.std(axis, dtype=dtype).reshape(1,-1)
    elif axis == 1:
        mean = X.mean(axis, dtype=dtype).reshape(-1,1)
        std = X.std(axis, dtype=dtype).reshape(-1,1)
    elif axis == 99:
        mean = X.mean(dtype=dtype)
        std = X.std(dtype=dtype)

    result = (X-mean)/std
    return result


def save_ndarray(X, filename="test.npy"):
    np.save(file=filename, arr=X)


def boolean_index(X, condition):
    result = np.where(eval(str("X")+condition))
    return result


def find_nearest_value(X, target_value):
    distance = np.abs(X-target_value)
    index = np.argmin(distance)
    return X[index]


def get_n_largest_values(X, n):
    X.sort()
    X=X[::-1]
    return X[:n]
