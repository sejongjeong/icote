N = int(input())
s = list(map(int, input().split()))
dp = [s[0], max(s[0], s[1])]

for i in range(2, N):
    dp.append(max(dp[i - 1], dp[i - 2] + s[i]))

print(dp[N - 1])
