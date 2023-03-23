# 이코테 35번 못생긴 수 / DP

n = int(input()) # 몇번째 수인지 받아줌

def ugly_number(n):
    ugly_lst = [1] # 리스트를 생성 후 못생긴 수를 저장해줌 / 1은 초기에 삽입

    for i in range(1000):
        ugly_lst += [ugly_lst[i] * j for j in [2,3,5]]

    ugly_lst = list(set(ugly_lst)) # 중복 제거 후 정렬
    ugly_lst.sort()

    return print(ugly_lst[n-1])

ugly_number(n)