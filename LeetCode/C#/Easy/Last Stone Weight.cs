public class Solution {
    public int LastStoneWeight(int[] stones) {
        var sl = stones.ToList();
        
        int first = 0, second = 0, smash = 0;
        
        while(sl.Count > 1) {
            first = sl.Max(); sl.Remove(sl.Max());
            second = sl.Max(); sl.Remove(sl.Max());
            
            smash = Math.Abs(first - second);
            if (smash != 0) 
                sl.Add(smash);
        }
        
        return sl.Count > 0 ? sl[0] : 0;
        
        
    }
}