public class Solution {
    public int Reverse(int x) {
        
        int sign = x > 0 ? 1 : -1;
        x = x > 0? x: -x;
        int result = 0;
        while(x > 0) {
            if(result > (Math.Pow(2,31)-1)/10 || result < (-1 * Math.Pow(2,31))/10)
                return 0;
            result = result * 10 + x%10;
            x /= 10;
        }
        return result*sign;
    }
}