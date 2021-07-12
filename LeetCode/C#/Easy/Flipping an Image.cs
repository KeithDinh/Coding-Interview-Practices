public class Solution {
    public int[][] FlipAndInvertImage(int[][] image) {
        var result = new List<int[]>();
        foreach(int[] i in image){
            var temp = i.Reverse().ToArray();
            for(int j = 0; j < temp.Length; j++) {
                temp[j] = temp[j] == 1 ? 0 : 1;
            }
            result.Add(temp);
        }
        return result.ToArray();
    }
}