class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.strip().split(' ')

        return len(new_s[-1])