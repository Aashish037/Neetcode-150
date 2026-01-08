class Solution:
    # Function to check if there are any duplicates in the list
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set();
        # Iterate through each number in the list
        for n in nums:
            # If the number is already in the hashset, return True
            if n in hashset:
                return True
            # Otherwise, add the number to the hashset
            hashset.add(n)
        
        # If the loop completes without returning True, return False
        return False
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)