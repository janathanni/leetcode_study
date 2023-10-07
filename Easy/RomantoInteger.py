class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1,
                      'V' : 5,
                      'X' : 10,
                      'L' : 50,
                      'C' : 100,
                      'D' : 500,
                      'M' : 1000
                    }
        
        sum = 0
        i   = 0
        
        while i < len(s): 
            if i == len(s) - 1 :
                sum += roman_dict[s[i]]
                break 

            if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                sum += roman_dict[s[i]] 
                i += 1 
            
            elif roman_dict[s[i]] < roman_dict[s[i+1]]:
                sum += (roman_dict[s[i+1]] - roman_dict[s[i]])
                i += 2 

        return sum 