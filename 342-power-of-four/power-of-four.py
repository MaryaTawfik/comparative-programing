class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 64=> 1*4=4
        #      4*4=16
        #      16*4=64
        if n == 1:
            return True
        def four(x):
            op = x * 4

            if op > n:
                return False
            if op == n:
                return True
            return four(op)
        return four(1)
            






        # if n == 1:
        #     return True
        # def is_power_of_four(x):
        #     res = x * 4
        #     if res > n :
        #         return False
        #     if res == n:
        #         return True
        #     return is_power_of_four(res)
        # return is_power_of_four(1)




        