class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        
        stack = []
        stackIndex = []
        validTrack = [0 for _ in range(len(s))]
        
        for i,e in enumerate(s):
            if e == "(":
                stack.append(e)
                stackIndex.append(i)
            elif e == ")":
                if stack and stack[-1] == "(":
                    validTrack[i] = 1
                    validTrack[stackIndex[-1]] = 1
                    stack.pop(-1)
                    stackIndex.pop(-1)
        count = []
        temp = 0
        for i in validTrack:
            if i == 0:
                count.append(temp)
                temp = 0
            else:
                temp += 1
        count.append(temp)
        return max(count)