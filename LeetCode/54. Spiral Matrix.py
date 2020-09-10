class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        num_row = len(matrix)
        num_col = len(matrix[0])
        res = []
        zone = 0
        num_elements = (num_row * num_col)
        while len(res) < num_elements:
            # move right
            for i in range(zone,num_col-zone):
                res.append(matrix[zone][i])
            if len(res)==num_elements:
                return res
            # move down
            for row_idx in range(zone+1, num_row-zone):
                c = matrix[row_idx][num_col-zone-1]
                res.append(c)
            if len(res) == num_elements:
                return res
            # move left
            for j in range(num_col-zone-1,zone,-1):
                res.append(matrix[num_row-1-zone][j-1])
            if len(res) == num_elements:
                return res
            # move up
            for i in range(num_row-2-zone,zone,-1):
                res.append(matrix[i][zone])
            if len(res) == num_elements:
                return res
            zone +=1
        return res
                
        