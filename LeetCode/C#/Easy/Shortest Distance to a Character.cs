public class Solution {
    public int[] ShortestToChar(string s, char c) {
        var locations = new int[s.Length];
        Array.Fill(locations, 0);
        
        int lastOccur = int.MinValue/2;
        for(int i=s.Length-1; i>=0; i--) {
            if(s[i] == c) {
                lastOccur = i;
            }
            locations[i] = Math.Abs(i - lastOccur);
        }

        lastOccur = int.MaxValue/2;
        for(int i=0; i < s.Length; i++) {
            if(s[i] == c) {
                lastOccur = i;
            }
            locations[i] = Math.Min(locations[i],  Math.Abs(i-lastOccur));
        }
        
        return locations;
    }
}