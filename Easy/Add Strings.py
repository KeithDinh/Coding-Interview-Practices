class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        carry = 0
        
        length1 = len(num1)
        length2 = len(num2)
        
        while length1 > 0 or length2 >0:
            temp = carry
            if length1 > 0:
                temp += int(num1[length1 - 1])
            
            if length2 > 0:
                temp += int(num2[length2 - 1])
                
            carry = int(temp / 10) # get the 1st digit
            result = (str(int(temp % 10))) + result # get the 2nd digit
            length1 -= 1
            length2 -= 1
        
        result = str(carry) + result if carry > 0 else result
        return result