import numpy as np

def gauss(a):
    n = len(a)
    A = [row[:] for row in a]
    x = n*[0]
    det = 1
    swaps = 0


    #приводим матрицу к треугольному виду (прямой ход)
    for i in range(n):
        if A[i][i] == 0:
            f = False
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    swaps += 1
                    print(swaps)
                    f = True
                    break
            if not f:
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
        round(x[i], 2)

    M = [row[:-1] for row in a]
    N = [row[-1] for row in a]
    res = [round(sum(M[i][j] * x[j] for j in range(n)) - N[i], 2) for i in range(n)]
    det *= (-1)**swaps

    print("решение системы: ", x)
    print("определитель матрицы: ", round(det,2))
    print("вектор невязок: ", res)
    print("количество перестановок: ", swaps)

def numpy_solution(a):
    print("-"*20)
    A = np.array([row[:-1] for row in a])
    B = np.array([row[-1] for row in a])

    try:
        X = np.round(np.linalg.solve(A, B), 2)  # решение системы
        det = round(np.linalg.det(A), 2)  # определитель матрицы
    except np.linalg.LinAlgError:
        print("матрица вырождена")
        return None, None
    print("решение numpy: ")
    print("решение системы: ", X)
    print("определитель матрицы: ", det)

#главная функция,
def main():
    choice = input("Ввод матрицы с клавиатуры (1) или из файла (2): ")

    if choice == "1":
        a = keyboard_read()
    elif choice == "2":
        a = file_read()
    else:
        print("Неверный ввод")
        return

    if not a:
        return

    result = check(a)
    print(result)
    if "несовместна" in result:
        return
    elif "бесконечное число решений" in result:
        return
    else:
        gauss(a)
        numpy_solution(a)


#чтение матрицы из файла
def file_read():
    filename = input("введите имя файла: ")
    with open(filename) as f:
        n = int(f.readline().strip())
        a = [list(map(int, f.readline().split())) for _ in range(n)]
    return a

def keyboard_read():
    n = int(input("введите размерность матрицы: "))
    print("введите расширенную матрицу: ")
    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    return a

def check(matrix):
    n = len(matrix)
    # Проверка на несовместность
    for row in matrix:
        if all(x == 0 for x in row[:-1]) and row[-1] != 0:
            return "Система несовместна"

    # Проверка на нулевые столбцы (ранг меньше n)
    rank = 0
    for i in range(n):
        # Проверяем, есть ли ненулевой элемент в столбце i среди строк >=i
        col_nonzero = False
        for j in range(i, n):
            if matrix[j][i] != 0:
                col_nonzero = True
                break
        if not col_nonzero:
            return "Система имеет бесконечное число решений"

    return "Система совместна и имеет единственное решение"

main()