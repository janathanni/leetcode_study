class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = list(map(str, digits))

        answer_int = int(''.join(str_digits)) + 1

        answer = map(int, list(str(answer_int)))

        return answer