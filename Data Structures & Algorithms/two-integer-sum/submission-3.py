class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def brute_force(nums, target):
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    if nums[i] + nums[j] == target:
                        return [i, j]

        def optimal(nums, target):
            indices = {}
            # for indices of nums in array
            for i, n in enumerate(nums):
                indices[n] = i

            for i, n in enumerate(nums):
                diff = target - n
                if diff in indices and indices[diff] != i:
                    return [i, indices[diff]]
            return []

        def optimal_one_pass(nums, target):
            prev_map = {}

            for i, n in enumerate(nums):
                diff = target - n
                if diff in prev_map: return [prev_map[diff], i]
                prev_map[n] = i

        return optimal_one_pass(nums, target)
