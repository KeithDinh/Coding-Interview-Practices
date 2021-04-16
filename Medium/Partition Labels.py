class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastPos = dict()
        result = []
        
        # save last index of each character in the string
        for i in range(len(S)):
            lastPos[S[i]] = i
            
        i = 0
        while i < len(S):
            upperBound = lastPos[S[i]]
            tracking = 1
            
            # loop from start position of character at i to last index of it
            while i + tracking < upperBound:
                # if current char at i is char at i+tracking, increment tracking and continue
                if S[i+tracking] == S[i]:
                    tracking += 1
                    continue
                
                # if last position of a character in the range is greater than last index of character at i, update the bound
                if lastPos[S[i + tracking]] > upperBound:
                    upperBound = lastPos[S[i + tracking]]
                tracking += 1
            
            result.append(upperBound - i +1)
            i = upperBound + 1
        return result