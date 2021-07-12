public class Solution {
    public int CoinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Array.Fill(dp, amount+1);
        dp[0] = 0;
        
        for(int i=1 ;i< dp.Length; i++) {
            foreach(int j in coins) {
                if(i >= j) {
                    dp[i] = Math.Min(dp[i], dp[i-j] + 1);
                }
            }
        }
        return dp[amount] == amount+1 ? -1 : dp[amount];
    }
}