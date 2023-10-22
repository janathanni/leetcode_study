class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                print(nums)
                j += 1
        
        return j