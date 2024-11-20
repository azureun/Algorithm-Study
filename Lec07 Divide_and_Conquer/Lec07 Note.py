# 분할 정복
'''
- 주어진 문제를 재귀 반복(recursion)을 활용하여 해결하려는 전략 방법
- 만약 문제 크기가 상대적으로 작은 경우 (base case) 반복 없이 직접적으로 해결

> 반대의 경우(recursive case) 3단계를 통해 수행됨
1. 분할(Divide) : 해결하기 쉽게 문제를 여러 개의 하위 문제로 나눔.
2. 정복(Conquer) : 나눈 하위 문제를 각각 해결함
3. 합병(Combine) : 하위 문제들 결과들을 합해 원래 문제에 대한 솔루션 구성함.
'''

# 분할 정복의 응용1: 거듭제곱(Exponentiation)
'''
- 지수(Exponent)의 크기 만큼 곱셈을 수행하는 연산
ex) C^4 = C x C x C x C 이므로 O(n)의 수행 시간 소요
분할 정복 적용 -> C^2 x C^2 = (C^2)^2 와 같이 표현 가능
-> 2번의 제곱 재귀(recursion)

거듭 제곱을 분할 정복을 이용하여 수행한 시간 복잡도 : O(logn)
'''

# 분할 정복 이용한 거듭제곱
def exponentiation(c, n):
    if n==0:
        return 1
    x = exponentiation(c, n//2)

    if n%2 == 0:
        return x*x
    else:
        return x * x * c
    
print(exponentiation(2, 256))

# 분할 정복의 응용2: 피보나치 수
'''
- 단순 재귀 호출 시 피보나치 시간 복잡도 : O(2^n)
- 분할정복기법 이용한 피보나치 시간 복잡도: O(logn)

'''

# 간단한 피보나치 수 구현
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(8))

########################################
# 분할 정복을 활용한 피보나치 수열

#분할
def multiply(F, M):
    x = (F[0][0] * M[0][0] + 
       F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + 
       F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1])
    
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w    

#정복
def power(F, n):
    if( n == 0 or n == 1):
        return
    M = [[1, 1], 
         [1, 0]]
    power(F, n // 2)
    multiply(F, F)

#병합
def fibonacci(n):
    F = [[1, 1]
         [1, 0]]
    if ( n == 0):
        return 0
    power(F, n-1)
    return F[0][0]

print(fibonacci(8))
########################################


# 분할 정복의 응용3: 행렬의 곱셈
'''
시간 복잡도 : O(n^3)
'''

# 단순한 행렬의 곱셈 알고리즘
def Simple_Matrix_Multiplication(A, B):
    C = [[0 for i in range(len(B(0)))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

A = [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]]
B = [[4,1,1,0],[103,79,104,86],[145,109,148,122],[187,139,192,158]]

# 분할 정복 기반 행렬의 곱셈 알고리즘
def marge_matrix(A, B):
    return [rowa + rowb for rowa, rowb in zip(A, B)]

def MatAdd(A, B):
    result = [[0 for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            result[i][j] = A[i][j] + B[i][j]
    return result

def createSubmatrices(A, starting_index, rows, columns):
    result = [[0 for i in range(rows)]for i in range(columns)]
    for i in range(rows):
        for j in range(columns):
            result[i][j] = A[starting_index[0] + i][starting_index[1] + j]
        return result
    
def MMRecursive(A, B, n):
    if (n == 1):
        return [[A[0][0]] * B[0][0]]
    else:
        # 분할
        A11, B11 = createSubmatrices(A, (0,0), n//2, n//2), createSubmatrices(B, (0,0), n//2, n//2)
        A12, B12 = createSubmatrices(A, (0,n//2), n//2, n//2), createSubmatrices(B, (0,n//2), n//2, n//2)
        A21, B21 = createSubmatrices(A, (n//2,0), n//2, n//2), createSubmatrices(B, (n//2, 0), n//2, n//2)
        A22, B22 = createSubmatrices(A, (n//2,n//2), n//2, n//2), createSubmatrices(B, (n//2,n//2), n//2, n//2)
        
        # 정복
        C11 = list(MatAdd(MMRecursive(A11, B11, n//2), MMRecursive(A12, B21, n//2)))
        C12 = list(MatAdd(MMRecursive(A11, B12, n//2), MMRecursive(A12, B22, n//2)))
        C21 = list(MatAdd(MMRecursive(A21, B11, n//2), MMRecursive(A22, B21, n//2)))
        C22 = list(MatAdd(MMRecursive(A21, B12, n//2), MMRecursive(A22, B22, n//2)))

        # 병합
        return marge_matrix(C11, C12) + marge_matrix(C21, C22)

A = [[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]]
B = [[4,1,1,0],[1,0,9,8],[9,8,7,6],[7,6,5,4]]

C = MMRecursive(A, B, 4)        
print(C)

########################################
