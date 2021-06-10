int avoidObstacles(int[] inputArray) {
    Array.Sort(inputArray);
    int n = 2;
    while(n > 0) {
        bool flag = true;
        int i = n;
        while(i <= inputArray.Last() && flag){
            if(inputArray.Contains(i)) {
                flag = false;
            }
            i += n;
        }
        if(flag == true) {
            break;
        }
        n++;
    }
    return n;
    
}
