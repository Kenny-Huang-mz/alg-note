def matrix_multiply(A, B,mod):
    rows_A,cols_A,cols_B=len(A),len(A[0]),len(B[0])
    res=[[0]*cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                res[i][j]+=(A[i][k]*B[k][j])%mod
                res[i][j]%=mod
    return res

def matrix_power(matrix, n,mod=int(1e9+7)):
    rows, cols=len(matrix), len(matrix[0])
    result=[[1 if i==j else 0 for j in range(cols)] for i in range(rows)]
    while n:
        if n%2:
            result=matrix_multiply(result, matrix,mod)
        matrix=matrix_multiply(matrix, matrix,mod)
        n//=2
    return result

# 示例使用
matrix = [[1, 1], [1, 0]]  # 斐波那契数列的矩阵形式
n = 5  # 计算第5个斐波那契数
result = matrix_power(matrix, n)
fibonacci_number = result[0][1]  # 结果矩阵的第一行第二列即为斐波那契数
print(fibonacci_number)