import math

def max_wire_length(w, heights):
    N = len(heights)
    dp = [[0] * (max(heights) + 1) for _ in range(N)]

    for h in range(1, heights[0] + 1):
        dp[0][h] = 0

    for i in range(1, N):
        for h1 in range(1, heights[i-1] + 1):
            for h2 in range(1, heights[i] + 1):
                length = math.sqrt((h2 - h1) ** 2 + w ** 2)
                dp[i][h2] = max(dp[i][h2], dp[i-1][h1] + length)

    return round(max(dp[N-1]), 2)


w = 4
heights = [100, 2, 100, 2, 100]
print(max_wire_length(w, heights))



