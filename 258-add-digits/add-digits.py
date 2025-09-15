class Solution:
    def addDigits(self, num: int) -> int:
        if num%9==0 and num!=0:
            return 9
        elif num==0:
            return 0
        else:
            return num%9
        