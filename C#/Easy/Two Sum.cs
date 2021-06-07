public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        var d = new Dictionary<int,int>();

        for(int i=0; i<nums.Length; i++) {
            int result = target - nums[i];
            if(d.ContainsKey(result) && i!= d[result]){
                return new int[2]{d[result], i };
            } else {
                d.Add(nums[i],i);
            }
        }
        
        return null;
    }
}