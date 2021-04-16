class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        arr = [0] * len(rooms)
        self.unlockRoom(rooms, 0, arr)
        for i in arr:
            if i == 0:
                return False
        return True
        
    
    def unlockRoom(self, rooms, roomIndex, arr):
        if arr[roomIndex] == 1:
            return
        else:
            arr[roomIndex] = 1
            for i in rooms[roomIndex]:
                self.unlockRoom(rooms, i, arr)