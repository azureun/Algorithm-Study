# 4.1 Bubble Sort
# 4.2 straight selection sort 단순 선택 정렬

## 4.1 Bubble Sort

# 4.1.1 Bubble Sort

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:    # a: MutableSequence -> 상수 변수
    n = len(a)      # 버블 정렬 시작
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:                   # a[j-1]이 a[j]보다 크다면
                a[j-1], a[j] = a[j], a[j-1]     # a[j-1]에는 a[j]를, a[j]에는 a[j-1]을 대입

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

        bubble_sort(x)  #배열 x를 버블 정렬
        print('오름차순으로 정렬 했습니다.')

        for i in range(num):
            print(f'x[{i}] = {x[i]}')          # 출력 형태 : x[i] = 숫자 값


