# 2.1 알고리즘 성능 지표 - "작업량", 정확성, 메모리, 단순성, 최적성
# 2.2 실험적 성능 측정 방법 및 그 한계
# 2.3 알고리즘 분석에 사용되는 대표 7가지 함수
# 2.4 점근 표기법 - BigO, BigOmega, BigTheta

## 2.4.1 BigO 표기법 - 삽입 정렬(Insert Sort)의 수행 시간 분석

def insertSort(arr):
    n = len(arr)
    print('loop 시작 전: ', arr)
    for i in range(1,n):
        print('\n{}번째 loop 시작\n'.format(i))
        print('S=',arr[:i], 'U=', arr[i:], '\t# {}번째 loop에서 정렬 전'.format(i))
        val = arr[i]                                # arr의 첫번째 원소부터 val에 저장
        pos = i                                     # i번째 인덱스 저장
        while pos > 0 and arr[pos-1] > val:         # pos 인덱스가 0보다 크고 arr[pos-1] 원소가 val 원소보다 크면
            arr[pos] = arr[pos-1]                   # arr[pos]에 arr[pos-1] 저장
            print('S=',arr[:i], 'U=', arr[i:])
            pos = pos - 1
        if pos == i:                # pos와 i가 같다면 pass
            pass
        else:
            arr[pos] = val          #아니면 val을 다시 arr[pos]에 저장
            print('S=', arr[:i],'U=', arr[i:])
        print('S=', arr[:i+1], 'U=', arr[i+1:], '\t# {}번째 loop에서 정렬 후'.format(i))
    print('\n정렬 종료')

arr = [48,43,42,32,26,12,8]
print("<arr 배열 목록>\n->", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print("\n\ninsertSort() 함수 실행!\n")
insertSort(arr)


## 2.4.2 선형 함수(Linear Function) 예시 - biggest 찾기
'''
def find_max(data):
    # Return the maximum element from a nonempty Python list
    biggest = data[0]               #The initial value to beat
    for i in range(1, len(data)):
        #for val in data:        #For each value:
        if data[i] > biggest:       #if it is greater than the best so far,
            biggest = data[i]       #we have found a new best (so far)
    return biggest

Data = [3,4,42,6,7,-1]
print("In Data array, biggest element is ", find_max(Data))
'''

## 2.4.3 이차 함수(Quadratic-Time) 예시 - 누적 평균(Perfix average) 구하기 O(n^2)
'''
# S의 누적 평균
# 1, 2, 3, 4, 5, 6, 7
# -> 1/1=1.0, (1+2=3)/2=1.5, (1+2+3=6)/3=2.0, (1+2+3+4=10)/4=2.5, ... , 28/7=4.0
S = [1,2,3,4,5,6,7]

def perfix_average1(S):
    # Return list such that, for all j, A[j] equals average of S[0], ... , S[j]
    n = len(S)  #O(1)
    A = [0]*n   #O(n)
    for j in range(n):  #O(n)
        total = 0                   # begin computing S[0] + ... + S[j]
        for i in range(j+1):        # 1+2+3+...+n=n(n+1)/2 -> O(n^2)
            total = total + S[i]
        A[j] = total / (j+1)        #record the average
    return A

print(perfix_average1(S))

# - 내부 루프 sum(S[0:j+1])로 간단히 표현.
# - 여전히 시간 복잡도 : O(n^2)
def perfix_average2(S):
    # Return list such that, for all j, A[j] equals average of S[0], ... , S[j]
    n = len(S)
    A = [0]*n
    for j in range(n):          #j=0 ~ j=7
        A[j] = sum(S[0:j+1])/(j+1)
    return A

print(perfix_average2(S))
'''

## 2.4.4 이차 함수(Quadratic-Time) 예시 - 누적 평균(Perfix average) 구하기 O(n)
# - total = S[0] + S[1] + ... + S[j] >> Recursion, 재귀로 나타냄.
'''
def perfix_average(S):
    #Return list such that, for all j, A[j] equals average of S[0], ... , S[j]
    n = len(S)  #O(1)
    A = [0]*n   #O(n)   Create new list of n zeros
    total = 0
    for j in range(n):  #O(n)
        total += S[j]   #O(1)
        A[j] = total/(j+1)  #O(1)
    return A
'''

## 2.4.5 삼차 함수(Cubic Function) 예시 - 리스트의 길이 모두 n인 집합 A,B,C에 대해 서로소(공집합)를 찾는 문제
# - worst case : O(n^3)
'''
A = [1,2,3]
B = [7,8]
C = [1,2]

def disjoint1(A,B,C):
    #Return True if there is no element common to all three lists
    for a in A:             # O(n)
        for b in B:         # O(n)
            for c in C:     # O(n)    -> 최종 : O(n^3)
                if a==b==c:
                    return False    # 공통된 값을 찾으면 False 반환
    return True                     # 모든 원소들 반복문 돌았을 때 공통된 원소가 없으면 True 반환

def disjoint2(A, B, C):
    #Return True if there is no element common to all three lists
    for a in A:             #O(n)
        for b in B:         #O(n)
            if a==b:        #O(1)  a와 b가 맞지 않으면 반복문 멈춤. -> O(n^2)만에 끝남.
                for c in C:
                    if a==c:
                        return False    # 공통된 값을 찾으면 False 반환
    return True                     # 모든 원소들 반복문 돌았을 때 공통된 원소가 없으면 True 반환

print("disjoint1 결과 : ", disjoint1(A, B, C))
print("disjoint2 결과 : ", disjoint2(A, B, C))
'''

## N-log-N 함수(N-log-N function) 예시
# - 1.분할 정복(divide and Conquer) & 2. 재귀 알고리즘(recursive algorithm) 사용함.
# - 피벗(pivot, 기준값)을 정함.
# (pivot > value) 인 경우는 value를 pivot보다 앞에, (pivot < value) 인 경우는 value를 pivot보다 뒤에 오게 함.

# <quick sort 특징>
# python의 list.sort()나 프로그래밍 언어 차원에서 기본적으로 지원되는 내장 정렬 함수 -> 대부분 quick sort 사용.
# 일반적으로 원소 개수가 적어질수록 좋지 않은 중간값 선택 확률 증가. -> 원소 개수에 따라 (quick sort + other sort) 혼합 사용.

# <quick sort의 시간 복잡도>
# - quick sort 성능 : pivot 값을 어떻게 선택 하느냐에 크게 달라질 수 있음.
# 이상적인 경우 : O(nlogn) -> pivot 값 기준으로 "동일한 개수"의 작은 값/큰 값들이 분할됨.
# 최악의 경우 : O(n^2) -> pivot 값 기준으로 "한 편으로 크게 치우치게" 되면, 성능 저하됨.
# -> 중앙값(median)에 가까운 pivot 값을 선택할 수 있는 섬세한 전략 요구됨.
# -> 배열의 첫 값/중앙 값/마지막 값 중, "크기가 중간인 값"을 사용하는 방법이 많이 사용됨.

## 퀵 정렬(quick sort) 구현
'''
def partition(lst, left, right):
    pivot = lst[(left + right)//2]   #pivot 설정
    print(f'Pivot = {pivot}')

    while left <= right:
        while (lst[left] < pivot):      #move left pointer to right
            left = left + 1
        while (lst[right] > pivot):     #move right pointer to left
            right = right - 1
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left, right = left + 1, right - 1
    return left

def quick_sort(lst, left, right):
    if left >= right:
        return

    partial = partition(lst, left, right)

    quick_sort(lst, left, partial-1)
    quick_sort(lst, partial, right)
    return lst

a = [3,7,8,5,2,4]
print(f"Input array: {a}")
p = partition(a, 0, len(a)-1)
print(f"Array after partitioning:{a}")

A = [24,10,30,13,20,27]
print(f"Original array A: {A}")
quick_sort(A, 0, len(A)-1)
print(f"Array A after quicksort: {A}")
'''