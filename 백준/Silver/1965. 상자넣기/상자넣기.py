n = int(input())
box = list(map(int, input().split()))
dp = [0] * 1000
if len(box) == 1:
    print(1)
else:
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if box[i] > box[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))