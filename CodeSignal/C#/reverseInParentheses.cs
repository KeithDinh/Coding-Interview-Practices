string reverseInParentheses(string inputString) {
    
    var s = new Stack<int>();
    char[] input = inputString.ToCharArray();
    
    for(int i=0; i<input.Length; i++) {
        if(input[i] == '(') {
            s.Push(i);
        } else if (input[i] == ')') {
            int startPos = s.Peek() + 1;
            s.Pop();
            char[] sa = input.Skip(startPos).Take(i - startPos).ToArray();
            string w = reverse(sa);
            for(int j=startPos, k=0; j<i && k <w.Length; j++, k++) {
                input[j] = w[k];
            }
        }
    }
    string resultString ="";
    foreach(char i in input) {
        if(i != '(' && i != ')'){
            resultString += i;
        }
    }
    return resultString;
}

string reverse(char[] c) {
    Array.Reverse(c);
    return new string(c);
}
