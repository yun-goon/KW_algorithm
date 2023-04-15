import random


def print_2d_array(arr):
    for row in arr:
        for item in row:
            print(item, end='\t')  # 각 요소를 탭으로 구분하여 출력
        print()  # 한 행이 끝나면 개행하여 다음 행 출력


def matrix_path2(n):
    c = [[random.randint(1, 11) for _ in range(n+1)] for _ in range(n+1)] # n+1 * n+1 배열, 범퍼 만들어줘야해서 , 각 값은 1~10
    for i in range(n+1):
        c[i][0] = 0
    for j in range(1,n+1):
        c[0][j] = 0
    print_2d_array(c)
    for i in range(1,n+1):
        for j in range(1,n+1):
            c[i][j] = c[i][j] + max(c[i-1][j],c[i][j-1])

    print_2d_array(c)
    return c[i][j]

print(matrix_path2(4))

