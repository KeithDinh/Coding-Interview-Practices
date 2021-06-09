class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [amount+1] * (amount+1)
        d[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i >= c:
                    d[i] = min(d[i], 1 + d[i-c])
        
        return d[amount] if d[amount] < amount+1 else -1