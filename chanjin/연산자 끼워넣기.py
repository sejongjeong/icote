# 이코테 19번 연산자 끼워넣기 dfs

import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 수의 개수
n_list = list(map(int, input().rstrip().split())) # A1,A2....An
operator = list(map(int, input().rstrip().split())) # 연산자 덧,뺄,곱,나 각각의 개수

min_val, max_val = int(1e9), int(-1e9) # 처음에 엄청 크고 작은 수로 초기화 후 비교를 통해 갱신
def solution(num, cnt, add, sub, mul, div):
    global min_val, max_val
    if cnt == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return

    if add > 0:
        solution(num + n_list[cnt], cnt+1, add-1, sub, mul, div)
    if sub > 0:
        solution(num - n_list[cnt], cnt+1, add, sub-1, mul, div)
    if mul > 0:
        solution(num * n_list[cnt], cnt+1, add, sub, mul-1, div)
    if div > 0:
        if num < 0:
            solution((num*(-1) // n_list[cnt])*(-1), cnt+1, add, sub, mul, div-1)
        else:
            solution(num // n_list[cnt], cnt+1, add, sub, mul, div-1)

solution(n_list[0], 1, operator[0], operator[1], operator[2], operator[3])
print(max_val)
print(min_val)