"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums."""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i, num in enumerate(nums):
            # [0, 1, 2, 3, 4, 5, 6]
            # [1, 2, 3, 4, 5, 7]
            # [0, 1, 2, 4, 5]
            if i == 0:
                if num != 0:
                    return 0
                continue
            if nums[i-1] != num-1:
                return num-1
        return len(nums)

