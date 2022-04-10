from itertools import permutations
import os


def output(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="\t")
        print()


def reverse_number(iterable):
    result = 0
    for i in range(len(iterable)):
        for j in range(i, len(iterable)):
            if iterable[i] > iterable[j]:
                result += 1
    return result


def determinant(m: list):
    if len(m) != len(m[0]):
        return None
    col_index = [i for i in range(len(m))]
    cols = list(permutations(col_index, len(col_index)))
    # print(cols)

    s = 0
    for n in range(len(cols)):
        # print(cols[n], type(cols[n]))
        temp = 1
        for r in range(len(m)):
            temp *= m[r][cols[n][r]]
        s += (-1) ** reverse_number(cols[n]) * temp
    return s


def input_matrix():
    r = int(input("请输入行数："))
    c = int(input("请输入列数："))
    if r != c:
        print("不是方阵，无法计算行列式")
        return None
    m = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            m[i][j] = int(input("请输入A[{}][{}]=".format(i + 1, j + 1)))
    return m


if __name__ == "__main__":
    # print(reverse_number((2, 1, 0)))
    # matrix = [[1, 0, 0, 0], [2, 3, 4, 4], [3, 4, 2, 1], [1, 1, 2, 3]]
    # ret = determinant(matrix)
    # print(ret)
    print("行列式计算器")
    matrix = input_matrix()
    if matrix is None:
        os.system("pause")
        exit(0)
    print("你输入的矩阵是：")
    output(matrix)
    ret = determinant(matrix)
    print("方阵A的行列式为", ret)
    os.system("pause")
