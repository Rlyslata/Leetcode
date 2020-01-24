from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums:
                try :
                    return [nums.index(nums[i]), nums.index(target - nums[i], nums.index(nums[i])+1)]
                except ValueError:
                    continue

        return []
