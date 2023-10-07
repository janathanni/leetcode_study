class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        string = str(x)

        indicator1 = 0
        indicator2 = len(string)-1

        while indicator1 < indicator2: 
            if string[indicator1] != string[indicator2]:
                return False 

            indicator1 += 1
            indicator2 -= 1  

        return True