class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x = str(x)
            x = int(x[0] + x[1:][::-1])
        else:
            x =  int(str(x)[::-1])
        if x > 2**31 or x < -2**31 :
            return 0
        return x 
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = -1 if x <0 else 1
        x = abs(x)
        while x != 0 :
            p = x % 10 
            x = x//10
            res = res * 10 +p
        if x > 2**31 or x < -2**31 :
            return 0
        return flag * res
            
