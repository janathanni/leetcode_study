class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = '' 

        strs.sort() 
        i = 0 

        while i < len(strs[0]) :
            for string in strs[1:]:
                if strs[0][i] != string[i]:
                    return prefix
            else:
                prefix += strs[0][i]
                i += 1    
            
        return prefix  