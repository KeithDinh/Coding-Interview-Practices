class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        d = {}
        
        # count the number of occurrence of each char
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in s:
            d[i] -= 1
            
            if i not in stack:
                # while loop check if we need to remove the itemS of stack and then 
                #   append current char i after the loop to make the smallest lexicographical
                    # 1st condition: if s not empty
                    # 2nd condition: if the occurence of i is not 0 (still have more)
                    # 3rd condition: if top of the stack has greater lexicographical order than i
                
                while stack and d[stack[-1]] > 0 and stack[-1] > i:
                    stack.pop()
                stack.append(i)
        
        
        return ''.join(stack)