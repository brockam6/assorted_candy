class Solution:
    """Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
        Input: arr = [4,3,1,1,3,3,2], k = 3
        Output: 2
        Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left."""
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        to_dict = {}
        for n in arr:
            if n in to_dict:
                to_dict[n] += 1
            else:
                to_dict[n] = 1

        ascending = sorted(to_dict, key=to_dict.get, reverse=False)

        for lowest in ascending:
            if k - to_dict[lowest] >= 0:
                if k - to_dict[lowest] == 0:
                    k = 0
                    del to_dict[lowest]
                    return len(list(to_dict.keys()))
                else: 
                    k -= to_dict[lowest]
                    del to_dict[lowest]
            else:
                k = 0
            if k == 0:
                break
        return len(list(to_dict.keys()))
            
