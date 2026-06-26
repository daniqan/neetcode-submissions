class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize binary search boundaries
        left, right = 0, len(nums) - 1
        
        # Continue while search space is valid
        while left <= right:
            mid = (left + right) // 2  # Find middle index
            
            # If target found at mid, return index
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # If target lies within left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Move search to left half
                else:
                    left = mid + 1   # Move search to right half
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Move search to right half
                else:
                    right = mid - 1  # Move search to left half
        
        # Target not found
        return -1