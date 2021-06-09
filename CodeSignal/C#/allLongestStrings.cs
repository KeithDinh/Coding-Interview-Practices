string[] allLongestStrings(string[] inputArray) {
    List<string> li = new List<string>(inputArray);
    
    int longest = inputArray.Max(s => s.Length);
    
    var biggestList = inputArray.Where(s => s.Length == longest);
    
    return biggestList.ToArray();
    
    
}
