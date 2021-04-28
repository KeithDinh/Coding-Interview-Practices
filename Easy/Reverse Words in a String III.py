class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        return ' '.join( [val[::-1] for val in s] )