class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        TOP, BOTTOM = 0, len(matrix)
        LEFT, RIGHT = 0, len(matrix[0])

        res = []
        while TOP < BOTTOM and LEFT < RIGHT:

            for i in range(LEFT, RIGHT):
                res.append(matrix[TOP][i])
            TOP += 1

            for i in range(TOP, BOTTOM):
                res.append(matrix[i][RIGHT-1])
            RIGHT -= 1

            if TOP < BOTTOM:
                for i in range(RIGHT-1, LEFT-1, -1):
                    res.append(matrix[BOTTOM-1][i])
                BOTTOM -= 1
            
            if LEFT < RIGHT:
                for i in range(BOTTOM-1,TOP-1,-1):
                    res.append(matrix[i][LEFT])
                LEFT += 1
        
        return res