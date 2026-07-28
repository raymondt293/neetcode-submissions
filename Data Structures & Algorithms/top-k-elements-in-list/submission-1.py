class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in num_count.items():
            buckets[count].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return res