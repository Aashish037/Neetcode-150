
from typing import List
from collections import defaultdict


# time complexity: O(n * k log k) where n is number of strings and k is max length of a string
# space complexity: O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        # Sort the string to create a key
        # Anagrams will have the same sorted representation
        for s in strs:
            key = ''.join(sorted(s)) 
            anagram_map[key].append(s)
        return list(anagram_map.values())
    
    
    # time complexity: O(n * k) where n is number of strings and k is max length of a string
    # space complexity: O(n * k)
    def groupAnagramsCounting(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        for s in strs:
            # Create a count array for 26 lowercase letters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Convert count array to a tuple to use as a key
            key = tuple(count)
            anagram_map[key].append(s)
        return list(anagram_map.values())