class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text1), len(text2)
        
        # dp = [[0] * (cols+1)] * (rows + 1)
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
                    
        return dp[-1][-1]