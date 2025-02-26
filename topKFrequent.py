from collections import Counter
from heapq import heappush, heappop
def topKFrequent(nums, k):
        # Count the frequency of each number in nums using Counter.
        num_frequencies = Counter(nums)
        # Initialize a min heap to keep track of top k elements.
        min_heap = []
        # Iterate over the number-frequency pairs.
        for num, freq in num_frequencies.items():
            # Push a tuple of (frequency, number) onto the heap.
            # Python's heapq module creates a min-heap by default.
            heappush(min_heap, (freq, num))
            # If the heap size exceeds k, remove the smallest frequency element.
            if len(min_heap) > k:
                heappop(min_heap)
        # Extract the top k frequent numbers by taking the second element of each tuple.
        top_k_frequent = [pair[1] for pair in min_heap]
        return top_k_frequent
        
print(topKFrequent([1,2,2,3,3,3], 2))
# output: [2,3]
print(topKFrequent([1,2,2,3,3,3], 1))
# output: [3]
print(topKFrequent([7,7], 1))
# output: [7]
