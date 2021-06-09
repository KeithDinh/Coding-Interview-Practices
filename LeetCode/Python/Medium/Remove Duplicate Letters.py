import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = collections.Counter(s)
        stack = []
        
        for c in s:
            d[c] -= 1
            
            # only add to stack if character doesn't exist in stack
            if c not in stack:

                # only pop if:
                    # 1st: stack not empty
                    # 2nd: stack top still have other occurrences
                    # 3rd: stack top is lexicographically greater than current character
                while stack and d[stack[-1]] != 0 and stack[-1] > c:
                    stack.pop(-1)
                stack.append(c)
        
        return ''.join(stack)