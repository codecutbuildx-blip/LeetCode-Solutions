from typing import List, Optional
import heapq

class Solution:
    def medianFinder(self, nums1: List[int], nums2: List[int]) -> None:
        """
        Approach: We use two heaps to store elements from both arrays.
        The smaller heap is used to store the smaller half of the numbers,
        and the larger heap is used to store the larger half. This way, we
        can always get the median in O(1) time by taking the average of
        the top element of the smaller heap and the root of the larger heap.
        
        Time Complexity: O(log(min(m,n))) where m and n are the sizes of nums1 and nums2 respectively.
        Space Complexity: O(m+n)
        """
        # Initialize two heaps, a min heap to store the smaller half and a max heap to store the larger half
        min_heap = []
        max_heap = []

        for num in nums1:
            heapq.heappush(min_heap, -num)  # Push the negative of the number onto the min heap
        for num in nums2:
            heapq.heappush(max_heap, num)

        # Merge the two heaps into one sorted list
        while len(min_heap) > len(max_heap):
            max_heap.append(-heapq.heappop(min_heap))  # Pop the top element from the min heap and push its negative back onto the max heap
        while len(max_heap) > len(min_heap):
            min_heap.append(-heapq.heappop(max_heap))  # Pop the root of the max heap and push it back onto the min heap

        # Balance the heaps to ensure the size difference is at most 1
        if len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # Return the median
        return (max_heap[0] if len(min_heap) == len(max_heap) else (-min_heap[0])) / 2