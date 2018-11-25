def vector_size_check(*vector_variables):
    return len(set([len(vector) for vector in vector_variables])) == 1


def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [element - sum(elements) for element, *elements  in zip(*vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha*element for element in vector_variable]

def matrix_size_check(*matrix_variables):
    return len(set([vector_size_check(*vectors) for vectors in zip(*matrix_variables)])) == 1 and len(set([len(matrix) for matrix in matrix_variables])) == 1


def is_matrix_equal(*matrix_variables):
    return max([max([len(set(elements)) for elements in zip(*vectors)]) for vectors in zip(*matrix_variables)]) == 1


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(elements) for elements in zip(*vectors)] for vectors in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[element - sum(elements) for element, *elements in zip(*vectors)] for vectors in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [[element for element in row] for row in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*element for element in vector] for vector in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return [len(col_a) for col_a in matrix_a][0] == [len(row_b) for row_b in zip(*matrix_b)][0]


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)] for row_a in matrix_a]
