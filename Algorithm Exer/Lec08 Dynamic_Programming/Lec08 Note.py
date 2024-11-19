# 동적 계획법 (DP) : 상향식 (Bottom Up)
'''
- 가장 작은 부붐문제부터 상위에 있는 문제로 풀어나가는 방법
- 문제의 각 단계의 부분 문제들은 그 이전 단계의 문제들의 답에 의존함.
- 한 번 푼 적 있는 부분 문제의 답 -> 다시 푸는 일이 없도록 테이블에 저장하여 재활용함. ex) 플로이드 워셔 알고리즘
'''

# 분할 정복 (DQ) : 하향식 (Top-Down)
'''
- 위에서부터 아래로 쪼개는 방법
- 쪼갠 각 부분 문제를 완전히 새로운 하나의 문제로 사용 가능
'''

# 동적 계획법으로 풀 수 있는 문제?
# -> 최적 부분 구조 & 중복되는 부분 문제

# 최적 부분 구조 (Optional Substructure)
'''
- 전체의 최적해가 부분 문제의 최적해로부터 만들어지는 구조
ex) A에서 C로 가는 최단 경로 문제 : A-B 최단 경로 + B-C 최단 경로
'''

# 중복되는 부분 문제 (Overlapping subproblems)
'''
전체 문제를 해결함에 있어 똑같은 부분문제가 중복되어 발생하는 문제
ex) 피보나치 수열
'''

# 재귀를 이용한 피보나치 수열
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(8))

# 동적 계획법을 활용한 피보나치 수열
def dp_fib(n, cache=dict()):
    #cache라는 메모리 변수 활용
    if n <= 2:
        cache[n] = 1
    if n in cache:
        return cache[n]
    # 리턴하기 전에 반드시 메모리에 기록해야 함.
    cache[n] = dp_fib(n-1, cache) + dp_fib(n-2, cache)
    return cache[n]
    
print(dp_fib(8))

# 피보나치 수열 알고리즘의 시간 복잡도
# - 간단한 재귀 방식: O(n^2)
# - 분할 정복 방식: O(logn)
# - 동적 계획법 방식: O(n)

######################

# 최장 공통 부분 순서(LCS; Longest Common Subsequence)
'''
- 공통 부분 순서는 두 순서 사이에 공통적으로 존재하는 부분 순서를 나타냄.
- 정렬되어 있는 개체의 목록에서 일부 요소를 제거한 것은 부분 순서(Subsequence)를 위미함.
- 최장 공통 부분 순서 :  여러 개의 공통 부분 순서 중 가장 긴 것
- 최장 공통 부분 순서 알고리즘 > 주로 두 데이터 비교에 유용함.
'''

# 재귀 방법을 이용한 LCS 구현 > 시간 복잡도 O(2^n)
def lcs(a,b,m,n):
    #print(m,n) #활성화 시 비교되는 문자의 인덱스 확인 가능.
    if m==0 or n==0:
        return 0
    elif a[m-1] == b[n-1]:
        return 1 + lcs(a,b,m-1,n-1)
    else:
        return max(lcs(a,b,m,n-1), lcs(a,b,m-1,n))

a = list("goodmorning")
b = list("gutenmorgen")
print(lcs(a, b, len(a), len(b)))

# 동적 계획법을 이용한 LCS 구현 > 시간 복잡도 O(mn)
def dp_lcs(a,b):
    table = [[0 for i in range(len(a)+1)] for j in range(len(a)+1)]

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])
    return table

a1 = list("goodmorning")
b1 = list("gutenmorgen")
dp_lcs_result = dp_lcs(a1, b1)
print(dp_lcs_result)
print(dp_lcs_result[len(a)][len(b)])

# LCS 등굣길 문제 - 프로그래머스 42898
def solution(m,n,puddles):
    dp = [[0 for i in range(m+1)] for j in range(n+1)] #dp 초기화
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [i, j] in puddles: #웅덩이 위치의 경우 값을 0으로
                dp[j][i] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])
    print(dp)
    return dp[n][m]
print(solution(4,3,[[2,2]]))

# LCS N으로 표현 문제 - 프로그래머스 42895
def N_solution(N, number):
    dp = []
    for num in range(1, 9): #1개부터 8개까지 확인
        all_case = set()
        all_case.add(int(str(N) * num)) # 이어 붙여서 만드는 경우 넣기 ex) {N}, {NN}, {NNN}...
        for i in range(num - 1):  # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in dp[i]:
                for op2 in dp[-i-1]:
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    all_case.add(op1 - op2)
                    if op2 != 0:
                        all_case.add(op1/op2)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in all_case:
            return num
        dp.append(all_case)
    return -1

print(N_solution(5,12))
print(N_solution(2,11))
                    
