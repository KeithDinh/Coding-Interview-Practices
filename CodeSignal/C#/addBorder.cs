string[] addBorder(string[] picture) {
    int row = picture.Length, col = picture[0].Length;
    
    string[] result = new string[picture.Length + 2];
    char[] horizontal = new char[col+2];
    Array.Fill(horizontal, '*');
    
    result[0] = new string(horizontal);
    result[result.Length - 1] = new string(horizontal);
    for(int i=1; i<result.Length-1; i++) {
        result[i] = '*' + picture[i-1] + '*';
    }
    
    return result;
}
