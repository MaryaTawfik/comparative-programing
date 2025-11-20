class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Recursive call: get the previous sequence
        prev = self.countAndSay(n - 1)
        
        # Build the current sequence using run-length encoding
        result = []
        i = 0
        while i < len(prev):
            count = 1
            # Count consecutive identical digits
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1
            # Append count + digit
            result.append(str(count))
            result.append(prev[i])
            i += 1
        
        return "".join(result)
