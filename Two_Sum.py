class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        default_index = 0
        default_number = nums[default_index]
        target_test = 0
        solution_list = []
        while True:
            restart = False
            for index in range(0, len(nums)):
                if default_number + nums[index] == target:
                    if default_index == index:
                        continue
                    else:
                        solution_list.append(default_index)
                        solution_list.append(index)
                        break
                elif index == len(nums) - 1 and default_number + nums[index] != target:
                    default_index = default_index + 1
                    restart = True
                    break
            if restart == True:
                default_number = nums[default_index]
                continue
            else:
                break
        return solution_list
