class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        breaker = False    #이중 for문을 빠져나가기 위해 만든 변수 
        tmp1    = 0        #정답을 담을 변수 
        tmp2    = 0        #정답을 담을 변수 
        for i in range (0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    tmp1    = i
                    tmp2    = j
                    breaker = True 
                    break
            if breaker == True:
                break 

        return [tmp1, tmp2]