# 이코테 29번 공유기 설치 / 이진 탐색

# 집의 개수 n, 공유기의 개수 c개를 받아줌
n,c = map(int, input().split()) 

# n번에 걸쳐 좌표를 받아준 후 정렬해줌(이진 탐색은 정렬이 기본 전제이기 때문)
house = [int(input()) for i in range(n)]
house.sort()

# 이진 탐색 함수 생성
def bin_search(house, start, end):
    result = 0 # 최종 결과물을 갱신을 통해 구함
    while start <= end:
        mid = (start+end)//2
        cnt = 1 # 공유기 수를 세어줌 / 처음엔 공유기를 설치한다고 가정
        
        val = house[0] # 맨 처음 좌표를 지정하고 갱신        
        for i in range(1,len(house)):
            if (house[i] - val) >= mid: # 거리 차이를 확인
                cnt += 1 # 공유기를 설치했다고 가정하고 카운트
                val = house[i] # 비교군을 갱신
        
        if cnt >= c: # 공유기 수가 더 많거나 같은 경우
            result = mid
            start = mid + 1
        else: # 공유기 수가 더 적은 경우 거리를 줄여줘야함
            end = mid - 1

    print(result)

# 거리를 기준으로 이진 탐색을 시작
start = 1
end = house[-1] - house[0]
bin_search(house, start, end)