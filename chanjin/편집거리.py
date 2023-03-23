# 이코테 36번 편집거리

# 문자를 받아서 리스트에 저장
a = list(input())
b = list(input())

# 연산 횟수를 계산
cnt = 0
while a != b:
    if len(a) == len(b): # replace 연산
        for i in range(len(a)): # a의 길이만큼 for문을 돌면서 비교하고, 교체해줌
            if a[i] != b[i]:
                a[i] = b[i] # 변경해줌
                cnt += 1 # 연산 횟수를 갱신해줌

    # 삽입, 삭제는 연산을 한번에 하나씩 하는 방식으로 진행
    if len(a) > len(b): # a의 길이가 더 긴 경우는 삭제 연산
        if a[:len(b)] == b[:]: # b의 길이까지 비교했을 때, a와 모두 같으면 비교한 바로 다음 값을 삭제
            a.pop(len(b))
            cnt += 1 # 연산 횟수 갱신
        else:
            for i in range(len(b)): # for문을 돌면서 비교 후 삭제해줌
                if a[i] != b[i]:
                    a.pop(i)
                    cnt +=1
                    break # 삭제 했으니 for문 돌지 않고 탈출, 한번에 하나의 연산을 하기 위함

    if len(a) < len(b): # a의 길이가 더 짧은 경우는 삽입 연산
        if a[:len(b)] == b[:]: # b의 길이까지 비교했을 때, a와 모두 같으면 비교한 바로 다음 값을 추가
            a.append(b[len(a)])
            cnt += 1 # 연산 횟수 갱신
        else:
            for i in range(len(a)): # for문을 돌면서 비교
                if a[i] != b[i]:
                    a.insert(i,b[i]) # i번째 위치에 값 추가
                    cnt +=1
                    break # 추가 했으니 더이상 for문을 돌지 않고 탈출, 한번에 하나의 연산을 하기 위함

print(cnt)