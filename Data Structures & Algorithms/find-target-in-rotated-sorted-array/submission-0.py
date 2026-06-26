class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Loop through each element in nums
        for i in range(len(nums)):
            # If current element equals target, return its index
            if nums[i] == target:
                return i
        # If not found, return -1
        return -1
