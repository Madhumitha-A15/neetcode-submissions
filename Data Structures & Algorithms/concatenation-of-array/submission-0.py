class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums) * 2
        ans = [0] * size
        
        for i in range(0 , len(nums)):
            ans[i] = nums[i]
        for i in range(len(nums) ,size):
            ans[i] = nums[i - len(nums)]
        
        return ans