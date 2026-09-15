class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count=0
        # for i in nums:
        return len(set(nums))<len(nums)