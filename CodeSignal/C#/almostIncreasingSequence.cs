    
bool almostIncreasingSequence(int[] sequence) {
    int r = 0;
    if (sequence[0] >= sequence[1]) {
        r += 1;
    }
    for(int i=2 ;i < sequence.Length; i++) {
        if(sequence[i-1] >= sequence[i]){
            r+=1;
            if(sequence[i-2] >= sequence[i]) {
                sequence[i] = sequence[i-1];
            }
        }
    }
    return r < 2;
}
