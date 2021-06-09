class Solution:
    def insert(self, intervals, newInterval):
        if not intervals or not intervals[0]:
            return [newInterval]
        if newInterval[0] > newInterval[1]:
            return intervals
         
        startIndex = endIndex = -1
        resultLower, resultUpper = [], []
        i,j = 0, len(intervals)-1
        updateI = updateJ = False
        while i <= j:
            if startIndex == -1:
                if (newInterval[0] <= intervals[i][0] or newInterval[0] in range(intervals[i][0],intervals[i][1]+1)):
                    startIndex = i
                    if newInterval[0] >= intervals[i][0]:
                        newInterval[0] = intervals[i][0]
                    updateI = True
                else:
                    resultLower.append(intervals[i])
                    i += 1
            
            if endIndex == -1:
                if (newInterval[1] >= intervals[j][1] or newInterval[1] in range(intervals[j][0],intervals[j][1]+1)):
                    endIndex = j
                    if newInterval[1] <= intervals[j][1]:
                        newInterval[1] = intervals[j][1]
                    updateJ = True
                else:
                    resultUpper.insert(0, intervals[j])
                    j -= 1
            
            if updateI and updateJ:
                break
        if startIndex == -1 or endIndex == -1:
            if newInterval[1] < intervals[0][0]:
                intervals.insert(0, newInterval)
                
            elif newInterval[0] > intervals[-1][1]:
                intervals.append(newInterval)
            
            elif newInterval[0] > intervals[i-1][1]:
                intervals.insert(i, newInterval)
                
            return intervals
    
        
        return resultLower + [[newInterval[0], newInterval[1]]] + resultUpper