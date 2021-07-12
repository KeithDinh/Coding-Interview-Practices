bool areSimilar(int[] a, int[] b) {
    if (a.Length != b.Length) return false;
    
    var pos = new List<int>();
    for(int i=0; i<a.Length; i++) {
        if(a[i] != b[i]) {
            pos.Add(i);
        }
        if(pos.Count > 2) {
            return false;
        }
    }
    if(pos.Count == 1) return false;
    else if (pos.Count == 0) return true;
    return (a[pos[0]] == b[pos[1]] && a[pos[1]] == b[pos[0]]);
    
}
