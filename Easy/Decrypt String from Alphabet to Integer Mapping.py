class Solution:
    def freqAlphabets(self, s: str) -> str:
        if s == '#':
            return ''
        result = list()
        asciiA = ord('a') - 1
        for i in range(len(s)):
            if s[i] == '#':
                result.pop()
                result.pop()
                result += chr(asciiA + int(s[i-2:i]))
            else:
                result += chr(asciiA + int(s[i]))
        
        return ''.join(result)