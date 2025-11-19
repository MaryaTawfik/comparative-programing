from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array with zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse iterate through both strings
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply digits
                mul = int(num1[i]) * int(num2[j])
                # Position in result array
                p1, p2 = i + j, i + j + 1
                # Add to existing value
                total = mul + result[p2]
                
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert result array to string, skipping leading zeros
        res_str = "".join(map(str, result)).lstrip("0")
        return res_str if res_str else "0"
