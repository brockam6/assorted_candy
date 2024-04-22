"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    
Example 2:
    Input: nums = [1], k = 1
    Output: [1]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heap will be used to find the most frequent appearing integers
        heap = []
        # Lookup counter will each unique int in the array and its corresponding number of appearences
        lookup_counter = {}
        for num in nums:
            if num in lookup_counter:
                lookup_counter[num] += 1
            else:
                lookup_counter[num] = 1
        # Push tuples containing int + number of appearances onto the heap for fastest retrieval of high number of appearences
        for key in lookup_counter:
            heapq.heappush(heap, (-lookup_counter[key], key))
        return [x[1] for x in heapq.nsmallest(k, heap)]
 
