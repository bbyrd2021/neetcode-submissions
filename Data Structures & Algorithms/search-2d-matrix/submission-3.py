class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary_search on both dimensions
        rows, cols = len(matrix), len(matrix[0])
        top, btm = 0, rows - 1

        while top <= btm:
            mid = (top + btm) // 2 
            if target < matrix[mid][0]:
                btm = mid - 1
            elif target > matrix[mid][cols - 1]:
                top = mid + 1
            else:
                break
        
        if top > btm:
            return False

        row = (top + btm) // 2

        l, r = 0, cols - 1
        while l <= r: 
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

        





        



        
            
            



