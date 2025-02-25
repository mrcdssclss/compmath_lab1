import numpy as np

def gauss(a):
    n = len(a)
    A = [row[:] for row in a]
    x = n*[0]
    det = 1
    swaps = 0
    M = [row[:-1] for row in a]
    N = [row[-1] for row in a]

    #приводим матрицу к треугольному виду (прямой ход)
    for i in range(n):
        if A[i][i] == 0:
            f = True
            for j in range(i + 1, n):
                if A[i][j] != 0:
                    f = False
                    break
            if f:
                print("матрица вырождена")
                return None, None, None, None

        det *= A[i][i]

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] -= A[i][k] * factor

    print("матрица в треугольном виде: ", A)

    #обратный ход
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j]*x[j]
        x[i] /= A[i][i]

    res = [sum(M[i][j] * x[j] for j in range(n)) - N[i] for i in range(n)]
    det *= (-1)**swaps

    print("решение системы: ", x)
    print("определитель матрицы: ", det)
    print("вектор невязок: ", res)

def numpy_solution(a):
    A = np.array([row[:-1] for row in a])
    B = np.array([row[-1] for row in a])

    try:
        X = np.linalg.solve(A, B)  # решение системы
        det = np.linalg.det(A)  # определитель матрицы
    except np.linalg.LinAlgError:
        print("матрица вырождена")
        return None, None
    print("решение системы: ", X)
    print("определитель матрицы: ", det)

#главная функция,
def main():
    choice = input("ввод матрицы с клавиатуры(1) или из файла(2): ")

    if choice == "1":
        keyboard_read()
    elif choice == "2":
        file_read()
    else:
        print("неверный ввод ")
        return


#чтение матрицы из файла
def file_read():
    filename = input("введите имя файла: ")
    with open(filename) as f:
        n = int(f.readline())
        a = [list(map(int, f.readline().split())) for _ in range(n)]

    gauss(a)
    numpy_solution(a)

def keyboard_read():
    n = int(input("введите размерность матрицы: "))
    print("введите расширенную матрицу: ")
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)

    gauss(a)
    numpy_solution(a)

main()