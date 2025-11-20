class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces
        s = s.rstrip()
        
        # Split by spaces and take the last word
        last_word = s.split()[-1]
        
        return len(last_word)
