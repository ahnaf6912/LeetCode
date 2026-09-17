class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        items_removed = 0
        for num in nums:
            if num == val:
                nums.remove(num)
                items_removed = items_removed + 1
        length = len(nums) - items_removed
        print(nums)
        print(length)