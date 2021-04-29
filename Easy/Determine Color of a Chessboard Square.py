class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - ord('a')) % 2 == 0:
            return True if int(coordinates[1]) % 2 == 0 else False
        else:
            return False if int(coordinates[1]) % 2 == 0 else True