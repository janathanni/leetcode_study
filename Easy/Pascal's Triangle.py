class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]
        
        cnt = 1 # items of row of index  or  row count of index, whatever it's same.
        current = [[1], [1,1]]

        while cnt < numRows-1 :
            tmp = []

            tmp.append(current[cnt][0])

            for i in range (0, cnt):
                tmp.append(current[cnt][i]+current[cnt][i+1])
            
            tmp.append(current[cnt][-1])

            current.append(tmp)

            cnt += 1
        
        return current