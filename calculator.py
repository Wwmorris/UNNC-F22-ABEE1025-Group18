import math
from tkinter import Tk, Menu, messagebox, Text, END
from re import findall
import numpy as np
from numpy.linalg import inv, solve
from numpy import zeros, dot
from os.path import exists


# matrix add
def matrix_add(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = [list() for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix_c_temp = matrix_a[i][j] + matrix_b[i][j]
            matrix_c[i].append(matrix_c_temp)
    return matrix_c


# matrix minus
def matrix_minus(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    matrix_c = [list() for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix_c_temp = matrix_a[i][j] - matrix_b[i][j]
            matrix_c[i].append(matrix_c_temp)
    return matrix_c


def matrix_divide(matrix_a, row, column):
    length = len(matrix_a)
    matrix_b = [list() for i in range(length // 2)]
    k = 0
    for i in range((row - 1) * length // 2, row * length // 2):
        for j in range((column - 1) * length // 2, column * length // 2):
            matrix_c_temp = matrix_a[i][j]
            matrix_b[k].append(matrix_c_temp)
        k += 1
    return matrix_b


# matrix merge
def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
    length = len(matrix_11)
    matrix_all = [list() for i in range(length * 2)]
    for i in range(length):
        matrix_all[i] = matrix_11[i] + matrix_12[i]
    for j in range(length):
        matrix_all[length + j] = matrix_21[j] + matrix_22[j]
    return matrix_all


# Matrix multiplication
def matrixMul(A, B):
    return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]


def det(array: list) -> int:
    """
	matrix det. type array : List[List[float]]
	"""
    assert len(array) == len(array[0])
    if len(array) == 1:
        return array[0][0]
    # Expand along the first column
    s = 0
    for i in range(len(array)):
        # Cofactor
        A = [array[j][1:] for j in range(len(array)) if j != i]
        if i % 2:
            s -= array[i][0] * det(A)
        else:
            s += array[i][0] * det(A)
    return s


# Strassen Alogithm
def strassen(matrix_a, matrix_b):
    # Judge whether the matrix is a power of 2
    def isPowerOf2(n):
        res = str(math.log2(n))
        return res.find(".") == len(res) - 2

    rows = len(matrix_a)
    rows2 = len(matrix_b)
    # Judge whether matrices A and B are powers of 2
    if (not isPowerOf2(rows)) or (not isPowerOf2(rows2)):
        return matrixMul(matrix_a, matrix_b)

    if rows == 1:
        matrix_all = [list() for i in range(rows)]
        matrix_all[0].append(matrix_a[0][0] * matrix_b[0][0])
    else:
        s1 = matrix_minus((matrix_divide(matrix_b, 1, 2)), (matrix_divide(matrix_b, 2, 2)))
        s2 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 1, 2)))
        s3 = matrix_add((matrix_divide(matrix_a, 2, 1)), (matrix_divide(matrix_a, 2, 2)))
        s4 = matrix_minus((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 1, 1)))
        s5 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 2)))
        s6 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 2, 2)))
        s7 = matrix_minus((matrix_divide(matrix_a, 1, 2)), (matrix_divide(matrix_a, 2, 2)))
        s8 = matrix_add((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 2, 2)))
        s9 = matrix_minus((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 1)))
        s10 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 1, 2)))
        p1 = strassen(matrix_divide(matrix_a, 1, 1), s1)
        p2 = strassen(s2, matrix_divide(matrix_b, 2, 2))
        p3 = strassen(s3, matrix_divide(matrix_b, 1, 1))
        p4 = strassen(matrix_divide(matrix_a, 2, 2), s4)
        p5 = strassen(s5, s6)
        p6 = strassen(s7, s8)
        p7 = strassen(s9, s10)
        c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
        c12 = matrix_add(p1, p2)
        c21 = matrix_add(p3, p4)
        c22 = matrix_minus(matrix_add(p5, p1), matrix_add(p3, p7))
        matrix_all = matrix_merge(c11, c12, c21, c22)
    return matrix_all


def Show_Info():
    if exists("Help.md"):
        pass
    else:
        messagebox.showinfo(title="Tips", message="Please see 'Help.md'")

def Martix_dot():
    """
    Matrix dot product operation
    :return:
    """
    global input_text
    global output_text
    output_text.delete(0.0, END)  # Delete the contents of the input box
    L = input_text.get(0.0, END)  # Get the new content of the input box

    Content1 = []
    Content2 = []
    Q = L.split('x')
    P1, P2 = Q[0], Q[1]
    P1 = P1.split('\n')
    P2 = P2.split('\n')
    # get the first matrix element
    for x in range(len(P1)):
        K1 = findall('[0-9]{1,}', P1[x])
        if len(K1) > 0:
            Content1.append(K1)
    A1 = zeros((len(Content1), len(Content1[0])), int)
    for x in range(len(Content1)):
        for y in range(len(Content1[0])):
            A1[x][y] = Content1[x][y]

    # get the second matrix element
    for x in range(len(P2)):
        K2 = findall('[0-9]{1,}', P2[x])  # find all number
        if len(K2) > 0:
            Content2.append(K2)
    A2 = zeros((len(Content2), len(Content2[0])), int)
    for x in range(len(Content2)):
        for y in range(len(Content2[0])):
            A2[x][y] = Content2[x][y]
    try:
        output_text.insert(0.0, dot(A1, A2))  # Render the result in the output box
    except:
        output_text.insert(0.0, "Invalid matrix input")


def Invertible_matrix():
    """
    Matrix inversion
    :return:
    """
    global input_text
    global output_text
    # Delete the contents of the output box
    output_text.delete(0.0, END)
    # Get the new content of the input box
    L = input_text.get(0.0, END)
    P = L.split('\n')
    Conten = []
    for x in range(len(P)):
        K = findall('[0-9]{1,}', P[x])
        if len(K) > 0:
            Conten.append(K)
    A = zeros((len(Conten), len(Conten[0])), int)
    for x in range(len(Conten)):
        for y in range(len(Conten[0])):
            A[x][y] = Conten[x][y]
    try:
        output_text.insert(0.0, inv(A))
    except:
        output_text.insert(0.0, "Invalid matrix input")


def Polynomial():
    """
    matrix polynomial
    :return:
    """
    global input_text
    global output_text
    output_text.delete(0.0, END)
    L = input_text.get(0.0, END)
    P = L.split('\n')
    Conten = []
    for x in P:
        if len(x) > 0:
            Conten.append(x.split())

    # get the matrix element
    A = zeros((len(Conten), len(Conten[0]) - 1))
    for x in range(len(Conten)):
        for y in range(len(Conten[0]) - 1):
            A[x][y] = int(Conten[x][y])
    B = []
    for x in range(len(Conten)):
        B.append(int(Conten[x][len(Conten[0]) - 1]))
    output_text.insert(0.0, solve(A, B))


def T():
    """
    matrix transpose
    :return:
    """
    global input_text
    global output_text
    output_text.delete(0.0, END)  # Delete the contents of the output box
    L = input_text.get(0.0, END)  # Get the new content of the input box
    P = L.split('\n')
    Conten = []
    # get the matrix element
    for x in range(len(P)):
        K = findall('[0-9]{1,}', P[x])  # fina all number
        if len(K) > 0:
            Conten.append(K)
    A = zeros((len(Conten), len(Conten[0])), int)
    for x in range(len(Conten)):
        for y in range(len(Conten[0])):
            A[x][y] = Conten[x][y]
    try:
        output_text.insert(0.0, A.T)
    except:
        output_text.insert(0.0, "Invalid matrix input")


def plus():
    """
    Matrix addition
    :return:
    """
    global input_text
    global output_text

    # delete the output content
    output_text.delete(0.0, END)
    # and get new input
    L = input_text.get(0.0, END)

    Content1 = []
    Content2 = []
    # split two matrix
    Q = L.split('+')
    # two matrix content
    matrix1_content, matrix2_content = Q[0], Q[1]
    # split the newline character
    matrix1_content = matrix1_content.split('\n')
    matrix2_content = matrix2_content.split('\n')
    for x in range(len(matrix1_content)):
        K1 = findall('[0-9]{1,}', matrix1_content[x])
        if len(K1) > 0:
            Content1.append(K1)
    # Assign values to matrix 1
    A1 = zeros((len(Content1), len(Content1[0])), int)
    for x in range(len(Content1)):
        for y in range(len(Content1[0])):
            A1[x][y] = Content1[x][y]

    # Temporary list stores matrix elements
    for x in range(len(matrix2_content)):
        K2 = findall('[0-9]{1,}', matrix2_content[x])
        if len(K2) > 0:
            Content2.append(K2)

    # Assign values to matrix 2
    A2 = zeros((len(Content2), len(Content2[0])), int)
    for x in range(len(Content2)):
        for y in range(len(Content2[0])):
            A2[x][y] = Content2[x][y]
    try:
        # Store results
        output_text.insert(0.0, A1 + A2)
    except:
        output_text.insert(0.0, "Invalid matrix input")


# matrix multiply
def multiply():
    """
    matrix multiply, input two matrix and calculate the result
    :return:
    """
    global input_text
    global output_text

    # delete the output content
    output_text.delete(0.0, END)
    # and get new input
    L = input_text.get(0.0, END)

    Content1 = []
    Content2 = []
    # split two matrix
    Q = L.split('*')
    # two matrix content
    matrix1_content, matrix2_content = Q[0], Q[1]
    # split the newline character
    matrix1_content = matrix1_content.split('\n')
    matrix2_content = matrix2_content.split('\n')
    for x in range(len(matrix1_content)):
        K1 = findall('[0-9]{1,}', matrix1_content[x])
        if len(K1) > 0:
            Content1.append(K1)
    # Assign values to matrix 1
    A1 = []
    for x in range(len(Content1)):
        row = []
        for y in range(len(Content1[0])):
            row.append(int(Content1[x][y]))
        A1.append(row)

    # Temporary list stores matrix elements
    for x in range(len(matrix2_content)):
        K2 = findall('[0-9]{1,}', matrix2_content[x])
        if len(K2) > 0:
            Content2.append(K2)

    # Assign values to matrix 2
    A2 = []
    for x in range(len(Content2)):
        row = []
        for y in range(len(Content2[0])):
            row.append(int(Content2[x][y]))
        A2.append(row)

    try:
        # Store results
        result = strassen(A1, A2)

        # initial output matrix
        output_matrix = zeros((len(result), len(result[0])), int)
        for x in range(len(result)):
            for y in range(len(result[0])):
                output_matrix[x][y] = result[x][y]
        # show result
        output_text.insert(0.0, output_matrix)
    except:
        output_text.insert(0.0, "Invalid matrix input")


def MatrixDet():
    """
    matrix transpose
    :return:
    """
    global input_text
    global output_text
    output_text.delete(0.0, END)  # Delete the contents of the output box
    L = input_text.get(0.0, END)  # Get the new content of the input box
    P = L.split('\n')
    Conten = []
    # get the matrix element
    for x in range(len(P)):
        K = findall('[0-9]{1,}', P[x])  # fina all number
        if len(K) > 0:
            Conten.append(K)
    A = []
    for x in range(len(Conten)):
        row = []
        for y in range(len(Conten[0])):
            row.append(int(Conten[x][y]))
        A.append(row)

    try:
        # get output result
        result = det(A)
        output_text.insert(0.0, result)
    except:
        output_text.insert(0.0, "Invalid matrix input")


def Matrix_Eigenvalue():
    """
    Find matrix eigenvalue
    :return:
    """
    global input_text
    global output_text
    output_text.delete(0.0, END)  # Delete the contents of the output box
    L = input_text.get(0.0, END)  # Get the new content of the input box
    P = L.split('\n')
    Conten = []
    # get the matrix element
    for x in range(len(P)):
        K = findall('[0-9]{1,}', P[x])  # fina all number
        if len(K) > 0:
            Conten.append(K)
    A = []
    for x in range(len(Conten)):
        row = []
        for y in range(len(Conten[0])):
            row.append(int(Conten[x][y]))
        A.append(row)

    try:
        # get output result
        eigenvalue, featurevector = np.linalg.eig(np.array(A))
        result = "Eigenvalue: " + str(eigenvalue) + "\n"+"Feature vector: \n" + str(featurevector)
        output_text.insert(0.0, result)
    except:
        output_text.insert(0.0, "Invalid matrix input")

def AdjointMatrix():
    """
    Adjoint matrix
    :return:
    """
    global input_text
    global output_text
    output_text.delete(0.0, END)  # Delete the contents of the output box
    L = input_text.get(0.0, END)  # Get the new content of the input box
    P = L.split('\n')
    Conten = []
    # get the matrix element
    for x in range(len(P)):
        K = findall('[0-9]{1,}', P[x])  # fina all number
        if len(K) > 0:
            Conten.append(K)
    A = []
    for x in range(len(Conten)):
        row = []
        for y in range(len(Conten[0])):
            row.append(int(Conten[x][y]))
        A.append(row)

    try:
        # get output result
        matrix = np.array(A)
        adjoint = np.linalg.det(matrix) * np.linalg.inv(matrix)
        # show result
        output_text.insert(0.0, str(adjoint))
    except:
        output_text.insert(0.0, "Invalid matrix input")


if __name__ == '__main__':
    Mywindow = Tk()  # Create GUI window

    Mywindow.title("Matrix Calculator")  # title
    Mywindow.geometry("800x450+500+250")  # size
    Mywindow.minsize(400, 400)  # min size

    input_text = Text(Mywindow, width=180, height=11, font=('Calibri 12  italic'))  # input textarea
    input_text.grid(row=0, column=0)  # grid
    input_text.insert(0.0, "Please enter matrix elements here...")  # Input prompt
    output_text = Text(Mywindow, width=180, height=20, font=('Calibri 12  italic'))  # output textarea
    output_text.grid(row=20, column=0)
    output_text.insert(0.0,
                       "After input, click the method to be calculated above, and the calculation results will be displayed here.")

    Menu_All = Menu(Mywindow)  # main menu
    MENU1 = Menu(Menu_All, tearoff=0)  # create main menu
    MENU1.add_command(label="Matrix inversion", command=lambda: Invertible_matrix())
    MENU1.add_command(label="Dot product of matrix", command=lambda: Martix_dot())
    MENU1.add_command(label="Polynomial solution", command=lambda: Polynomial())
    MENU1.add_command(label="Transpose matrix", command=lambda: T())
    MENU1.add_command(label="Add two matrices", command=lambda: plus())
    MENU1.add_command(label="Matrices multiply", command=lambda: multiply())
    MENU1.add_command(label="Matrices det", command=lambda: MatrixDet())
    MENU1.add_command(label="Matrices eigenvalue", command=lambda: Matrix_Eigenvalue())
    MENU1.add_command(label="Adjoint Matrix", command=lambda: AdjointMatrix())

    Menu_All.add_cascade(label="Select Operation Type", menu=MENU1, font=('Calibri 12 '))
    MENU2 = Menu(Menu_All, tearoff=0)  # main menu
    MENU2.add_command(label="Help Detail", command=lambda: Show_Info())
    Menu_All.add_cascade(label='Help', menu=MENU2, font=('Calibri 12 '))  # show all menu

    Mywindow.config(menu=Menu_All)
    Mywindow.mainloop()
