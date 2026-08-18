class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = nums[0]
        global_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum + nums[i] > nums[i]:
                curr_sum = curr_sum + nums[i]
            else:
                curr_sum = nums[i]
            
            global_sum = max(global_sum, curr_sum)
        
        return global_sum