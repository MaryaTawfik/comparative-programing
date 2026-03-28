class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(n):
            for j in range(i + 1, n):
                a = num[:i+1]
                b = num[i+1:j+1]
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue

                x = int(a)
                y = int(b)
                k = j + 1
                used = False  
                while k < n:
                    z = x + y
                    z_str = str(z)
                    if not num.startswith(z_str, k):
                        break
                    k += len(z_str)
                    x, y = y, z
                    used = True
                if k == n and used:
                    return True

        return False