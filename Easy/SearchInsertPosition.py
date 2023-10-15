class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_idx = 0 
        r_idx = len(nums)

        if target <= nums[0]:
            return 0
        
        elif target > nums[-1]:
            return r_idx
        
        while l_idx < r_idx:
            m_idx = (r_idx + l_idx)//2
            
            if target <= nums[m_idx] and target > nums[m_idx-1]:
                break  

            elif nums[m_idx] > target:
                r_idx = m_idx 
            # target > m_idx 
            else:
                l_idx = m_idx+1

        return m_idx         