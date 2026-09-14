class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        verification = 0
        if rec1[0] < rec2[2]:
            verification = verification + 1
        if rec1[2] > rec2[0]:
            verification = verification + 1
        if rec1[1] < rec2[3]:
            verification = verification + 1
        if rec1[3] > rec2[1]:
            verification = verification + 1
        if verification == 4:
            return True
        else:
            return False