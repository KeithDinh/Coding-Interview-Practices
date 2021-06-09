class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        
        for i in range(rows):
            image[i] = list(reversed(image[i]))
            for j in range(cols):
                image[i][j] += 1 if image[i][j] == 0 else -1
        
        return image