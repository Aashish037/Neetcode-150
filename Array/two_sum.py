from typing import List

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the number and its index: {value: index}
        numMap = {} 
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the value needed to reach the target
            complement = target - num
            
            # Check if the complement has already been seen (is in the map)
            if complement in numMap:
                # If found, return the index of the complement and the current index
                return [numMap[complement], i]
            
            # If not found, add the current number and its index to the map
            numMap[num] = i
        
        # This line is typically unreachable if a solution is guaranteed
        return []

# Example Usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(f"Input: {nums}, Target: {target}") # Output: [0, 1]
print(f"Output: {solution.twoSum(nums, target)}")