from typing import List, Optional
import heapq

class Solution:
    def medianFinder(self, nums1: List[int], nums2: List[int]) -> Optional[float]:
        """
        Approach: 
            We use two heaps to store elements from both arrays. The heap on the left is a max heap and the heap on the right is a min heap.
            When an element is added to the left heap, it will be pushed into the right heap if its size exceeds half of the total number of elements in both heaps.
            Similarly, when an element is added to the right heap, it will be pushed into the left heap if its size is less than or equal to half of the total number of elements in both heaps.
            The median can be calculated by taking the average of the top elements from both heaps.

        Time Complexity: O(log(m+n))
        Space Complexity: O(1)
        """
        
        # Initialize two heaps, one for max heap and one for min heap
        max_heap = []
        min_heap = []

        # Iterate through nums1 and nums2 simultaneously
        for num in nums1 + nums2:
            # If the size of max_heap is greater than or equal to the size of min_heap,
            # push the element into max_heap. Otherwise, push it into min_heap.
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            # Balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Calculate the median
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2
        else:
            return -max_heap[0]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.medianFinder([1, 3], [2]))  # Expected: 2.0
    print(s.medianFinder([1, 2], [3, 4]))  # Expected: 2.5