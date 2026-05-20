from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # def my_intuition(nums, k):
        #     count_map = defaultdict(int)

        #     for i in nums:
        #         count_map[i] += 1

        #     counts = count_map.items()

        #     sorted_counts  = sorted(counts, key=lambda x:x[1], reverse=True)

        #     res = []
        #     return [j[0] for j in sorted_counts[:k]]

        def my_optimal(nums, k):
            count_map = defaultdict(int)

            for i in nums:
                count_map[i] += 1
            counts = count_map.items()
            top_k = heapq.nlargest(k, counts, key=lambda x: x[1])

            return [j[0] for j in top_k]

        # return my_intuition(nums, k)
        return my_optimal(nums, k)





        
