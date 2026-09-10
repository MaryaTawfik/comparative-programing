class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        def is_power_of_four(x):
            res = x * 4
            if res > n :
                return False
            if res == n:
                return True
            return is_power_of_four(res)
        return is_power_of_four(1)




        