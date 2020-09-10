class Solution:
    def generateMatrix(self, n):
        res = [[0]* n for _ in range(n)]
        n_col = n
        n_row = n
        num_elements = n*n
        e = 0
        zone = 0
        data = 1
        while data <= num_elements:
            # move right 
            for i in range(zone, n_col - zone):
                res[zone][i] = data
                data +=1
            if data == num_elements+1:
                return res
            # move down
            for j in range(zone+1,n_row-zone):
                res[j][n_col-1-zone] = data
                data +=1
            if data == num_elements+1:
                return res
            # move left
            for i in range(n_col-1-zone,zone,-1):
                res[n_col-1-zone][i-1] = data
                data+=1
            if data == num_elements+1:
                return res
            # move up
            for j in range(n_row-2-zone,zone,-1):
                res[j][zone] = data
                data+=1
            if data == num_elements+1:
                return res
            zone +=1
        return res        