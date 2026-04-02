from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, k: int) -> List[List[int]]:
        res = []
        m = 0
        n = 0
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while True:
            for i in range(k):
                if not (m+k <= rows and n+k <= cols):
                    break
                res.append([m+n*i for _ in range(k)])
                m += k
            if m > rows or n > cols:
                break
            for j in d:
                if 0<=m+j[0]<rows and 0<=n+j[1]<cols:
                    res[-1].append(m+n)
                    m += j[0]
                    n += j[1]
            k += 1
        return res

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.spiralMatrixIII(3, 3, 1))  # Expected: [[0,1,2],[1,2,3],[2,3,4]]
    print(s.spiralMatrixIII(3, 3, 2))  # Expected: [[0,1,2],[1,2,3],[2,3,4],[0,1,2]]