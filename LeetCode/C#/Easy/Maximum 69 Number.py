class Solution:
    def maximum69Number (self, num: int) -> int:
        listNum = list(str(num))
        
        for i in range(len(listNum)):
            if listNum[i] == '6':
                listNum[i] = '9'
                break
        
        return ''.join(listNum)
    
    # str(num).replace('6','9',1)