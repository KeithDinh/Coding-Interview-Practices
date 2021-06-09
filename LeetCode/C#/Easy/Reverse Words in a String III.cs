public class Solution {
    public string ReverseWords(string s) {
        var arr = s.ToCharArray();
        Array.Reverse(arr);
        
        s = new string(arr);

        var arr2 = s.Split(' ');
        Array.Reverse(arr2);
        return string.Join(" ", arr2);
    
    }
}