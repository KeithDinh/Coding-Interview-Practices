public class Solution {
    public int LongestPalindrome(string s) {
        var d = new Dictionary<char,int>();
        foreach(char c in s.ToCharArray()){
            if (d.ContainsKey(c)) {
                d[c] += 1;
            } else {
                d.Add(c, 1);
            }
        }
        
        int result = 0;
        bool odd = false;
        foreach(char c in d.Keys){
            if(d[c] % 2 == 0){
                result += d[c];
            }
            else{
                odd = true;
                result += d[c] - 1;
            } 
        }
        
        return odd ? result + 1 : result;
    }
}