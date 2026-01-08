class Solution:
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    # Sorting Approach
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Hash Map Approach
    
    def isAnagramHashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        # Count characters in s
        # Increase count for characters in s
        # If a character is already in count, increase its count
        # Otherwise, initialize its count to 1
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Decrease count for characters in t
        # If any count goes below zero, return False
        # If a character in t is not found in count, return False
        # Finally, if all counts are zero, return True
        for char in t:
            if char in count:
                count[char] -= 1
                if count[char] < 0:
                    return False
            else:
                return False

    # Check if all counts are zero
        return True