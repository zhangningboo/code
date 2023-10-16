from typing import List


def solve(n: int, C: int, c: List[int], w: List[int]) -> int:
    dp = [[0] * (C + 1) for _ in range(2)]
    now, old = 0, 1
    for i in range(1, n + 1):
        now, old = old, now
        for j in range(C, -1, -1):
            if c[i] > j:
                dp[now][j] = dp[old][j]
            else:
                dp[now][j] = max(dp[old][j - c[i]] + w[i], dp[old][j])
    return dp[now][C]


c = [0, 2, 3, 6, 5]
w = [0, 6, 3, 5, 4]
n = len(c) - 1
C = 9

print(solve(n, C, c, w))