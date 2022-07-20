class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l1 = 0
        h1 = len(matrix[0])-1
        l2 = 0
        h2 = len(matrix) - 1
        
        while l2 < h2:
            m = l2 + (h2 - l2)//2
            if target <= matrix[l2][h1]:
                break
            
            elif target <= matrix[m][h1]:
                h2 = m 
            else:
                l2 = m + 1
        
        while l1 <= h1:
            m = l1 + (h1 - l1)//2
            if target == matrix[l2][m]:
                return True
                break
            elif target < matrix[l2][m]:
                h1 = m - 1
            else:
                l1 = m + 1
        
        return False
            
        
            
            
                
                
                
                
            