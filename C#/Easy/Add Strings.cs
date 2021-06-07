public class Solution {
    public string AddStrings(string num1, string num2) {
        int minLength = Math.Max(num1.Length, num2.Length);
        
        int[] n1 = Array.ConvertAll(num1.ToCharArray(), c => (int)Char.GetNumericValue(c));
        int[] n2 = Array.ConvertAll(num2.ToCharArray(), c => (int)Char.GetNumericValue(c));
        
        int carry = 0;
        
        string resultString = "";
        
        for(int i1=n1.Length-1, i2=n2.Length-1; i1>=0 || i2>=0; i1--, i2--) {
            int result = (i1 >= 0 ? n1[i1]: 0) + (i2 >= 0 ? n2[i2]: 0) + carry;
            carry = (result >= 10) ? 1 : 0;
            resultString = (result%10).ToString() + resultString;
        }
        
        resultString = (carry == 1)? '1' + resultString : resultString;
        
        return resultString;
    }
}