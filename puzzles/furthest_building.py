"""
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4

Explanation: Starting at building 0, you can follow these steps:
    - Go to building 1 without using ladders nor bricks since 4 >= 2.
    - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
    - Go to building 3 without using ladders nor bricks since 7 >= 6.
    - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders

"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # heights[0] first building
        # To move to next building:
            # If next is same height or greater, brick/ladders needed
            # If less, either use 1 ladder or next height minus current height bricks
            # return index of farthest reachable building
        heap = []
        for i, height_of_current in enumerate(heights):
            if i < len(heights) -1:
                current_diff = heights[i+1] - height_of_current
                print(f"I and current diff: {i} : {current_diff}")
                if current_diff <= 0:
                    continue
                bricks -= current_diff
                print(f"Brick count: {bricks}")
                heapq.heappush(heap, -current_diff)
                print(f"Heap: {heap}")
                if bricks < 0:
                    bricks += -heapq.heappop(heap)
                    print(f"Negative bricks: {bricks}")
                    ladders -= 1
                    print(f"Ladder in negative bricks: {ladders}")

                if ladders < 0:
                    print(f"Ladders less than 0: {i} : {ladders}")
                    return i
        return len(heights) - 1


s = Solution()
print(s.furthestBuilding(heights=[1,5,1,2,3,4,1000], bricks=4, ladders=1))

