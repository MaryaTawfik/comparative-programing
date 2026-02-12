from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_=Counter(ransomNote)
        magazine_=Counter(magazine)
        for key,val in ransomNote_.items():
            if val > magazine_[key]:
                return False
        return True



       


       