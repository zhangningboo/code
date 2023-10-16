# https://www.lintcode.com/problem/724/description
from typing import (
    List,
)

class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        # 转换为01背包问题
        n = sum(nums)
        C = n // 2
        N = len(nums)
        dp = [[0] * (C + 1) for _ in range(2)]
        now, old = 0, 1
        for i in range(1, N + 1):
            now, old = old, now
            idx = i - 1
            for j in range(1, C + 1):
                if nums[idx] > j:
                    dp[now][j] = dp[old][j]
                else:
                    dp[now][j] = max(dp[old][j], dp[old][j - nums[idx]] + nums[idx])

        return abs(dp[now][C] - (n - dp[now][C]))

