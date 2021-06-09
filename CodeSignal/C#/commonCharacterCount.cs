int commonCharacterCount(string s1, string s2) {
    var d = new Dictionary<char, int>();
    foreach(char c in s1.ToCharArray()) {
        if (d.ContainsKey(c)) {
            d[c] = d[c] + 1;
        } else {
            d.Add(c, 1);
        }
    }
    
    int count = 0;
    
    foreach(char c in s2.ToCharArray()) {
        if (d.ContainsKey(c)) {
            d[c] = d[c] - 1;
            count = (d[c] >= 0) ? count + 1: count;
        }
    }
    
    return count;
}
