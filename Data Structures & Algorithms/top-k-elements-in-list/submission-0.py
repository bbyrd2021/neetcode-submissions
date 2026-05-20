from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def my_intuition(nums, k):
            count_map = defaultdict(int)

            for i in nums:
                count_map[i] += 1

            counts = count_map.items()

            sorted_counts  = sorted(counts, key=lambda x:x[1], reverse=True)

            res = []
            for j in sorted_counts[:k]:
                res.append(j[0])
            return res

        return my_intuition(nums, k)



        
