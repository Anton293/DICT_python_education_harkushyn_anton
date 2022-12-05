"""matrix module"""
from random import randint
from typing import List, Any
import copy

ERROR = "\033[31m{}\033[0m"


def generate(width=1, height=1) -> list:
    """generate matrix from width and height"""
    return [[randint(0, 9) for i in range(0, height)] for j in range(0, width)]


def visual(matrix_array: list, result="") -> None:
    """output matrix user"""
    if matrix_array is None:
        print("ERROR: matrix")
    elif type(matrix_array) == list:
        for matrix_line in matrix_array:
            result += "\n" + " ".join([str(i) for i in matrix_line])
        print(result)
    else:
        print(matrix_array)


def multiplication(matrix_a: list, matrix_b: list):
    """multiplication matrix A and B"""
    if len(matrix_a) == len(matrix_b[0]):  # height A == width B
        length = len(matrix_a)
        result_matrix = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

        return result_matrix
    return None


def multiplication_on_constant(matrix_a: list, constant: int, action="*"):
    """constant matrix A"""
    try:
        length = len(matrix_a)
        result_matrix = [
            [eval(f"{num}{action}{constant}") for num in matrix_a[i]] for i in range(length)
        ]
        return result_matrix
    except ValueError:
        return None


def addition(matrix_a: list, matrix_b: list):
    """addition matrix A and B"""
    if len(matrix_a[0]) == len(matrix_b[0]) and len(matrix_a) == len(
            matrix_b):  # height A == height B and width A == width B
        length = len(matrix_a)
        result_matrix: List[List[Any]] = [
            [
                matrix_a[i][j] + matrix_b[i][j] for j in range(length)
            ] for i in range(length)
        ]
        return result_matrix
    return None


def transpose(matrix_a: list, type_transpose: int):
    """transpose matrix A"""
    height = len(matrix_a)
    width = len(matrix_a[0])
    result_matrix = [[0 for x in range(0, height)] for y in range(0, width)]
    for x in range(height):
        for y in range(width):
            if type_transpose == 1:
                result_matrix[x][y] = matrix_a[y][x]#\
            elif type_transpose == 2:
                result_matrix[y][x] = matrix_a[y][x]#/
            elif type_transpose == 3:
                result_matrix[y][x] = matrix_a[y][width-x-1]#|
            elif type_transpose == 4:
                result_matrix[y][x] = matrix_a[width-y-1][x]#-
    return result_matrix


############################################################################
#                                determinant                               #
############################################################################


def new_matrix(matrix_a: list, i: int) -> list:
    """find new matrix the determinant of matrix"""
    arr = copy.deepcopy(matrix_a)
    if len(arr) == 2:
        return arr
    arr.pop(0)
    for cell in arr:
        cell.pop(i)
    return arr


def determinant(matrix_a: list):
    """determinant of matrix"""
    if len(matrix_a) == 1:
        result_matrix = matrix_a[0]
        return result_matrix
    elif len(matrix_a) == 2:
        result_matrix = matrix_a[0][0] * matrix_a[1][1] - matrix_a[1][0] * matrix_a[0][1]
        return result_matrix
    else:
        result_matrix = 0
        for i in range(len(matrix_a[0])):
            result_matrix += ((-1) ** i) * matrix_a[0][i] * determinant(new_matrix(matrix_a, i))
        return result_matrix


################################################################
#                           inverse                            #
################################################################


def get_matrix_minor(matrix_a, i, j):
    return [row[:j] + row[j+1:] for row in (matrix_a[:i] + matrix_a[i + 1:])]


def cofactors_find(matrix_a):
    cofactors = []
    for i in range(len(matrix_a)):
        cofactor_row = []
        for j in range(len(matrix_a)):
            minor = get_matrix_minor(matrix_a, i, j)
            cofactor_row.append(((-1)**(i+j)) * determinant(minor))
        cofactors.append(cofactor_row)
    return cofactors


def division_on_determinant(cofactors, det):
    for i in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[i][j] = cofactors[i][j]/det
    return cofactors


def inverse(matrix_a):
    """inverse matrix"""
    det = determinant(matrix_a)
    if det == 0:
        print(ERROR.format("This matrix doesn't have an inverse."))
        return None
    #special case for 2x2 matrix:
    if len(matrix_a) == 2:
        return [[matrix_a[1][1] / det, -1 * matrix_a[0][1] / det],
                [-1 * matrix_a[1][0] / det, matrix_a[0][0] / det]]

    #find matrix of cofactors
    cofactors = cofactors_find(matrix_a)
    cofactors = transpose(cofactors, 1)
    cofactors = division_on_determinant(cofactors, det)
    return cofactors
