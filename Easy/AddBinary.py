class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ''

        bin1 = int(a, 2)
        bin2 = int(b, 2)

        return bin(bin1 + bin2)[2:]