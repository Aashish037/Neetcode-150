# 347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.
from ast import List

class Solution:
    # time complexity: O(N log N)
    # space complexity: O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency map
        # Count the frequency of each element
        freq_map= {}
        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num] = 1

        # Create a list of (element, frequency) pairs
        freq_list = []
        # Populate the frequency list
        for num, count in freq_map.items():
            freq_list.append((num, count))

        # Sort the list based on frequency in descending order
        freq_list.sort(key= lambda x:x[1], reverse = True)

        # Extract the top k frequent elements
        result = []
        # Collect the top k elements
        for i in range(k):
            result.append(freq_list[i][0])

        return result



# bucket sort approach
    # time complexity: O(N)
    # space complexity: O(N)
    def topKFrequent_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency map
        freq_map= {}
        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num] = 1

        # Create buckets where index represents frequency
        max_freq = max(freq_map.values())
        buckets = [[] for _ in range(max_freq + 1)]

        # Populate the buckets
        for num, count in freq_map.items():
            buckets[count].append(num)

        # Gather the top k frequent elements
        result = []
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result