from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars=Counter(chars)
        length=0
        for i in words:
            freq=Counter(i)
            for key, val in freq.items():
                if key in chars and val<=chars[key]:
                    continue
                else:
                    break
            else:
                length+=len(i)
        return length


        