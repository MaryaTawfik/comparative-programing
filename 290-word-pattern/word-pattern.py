from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_=s.split()
        if len(s_) != len(pattern):
            return False
        ch_word=defaultdict(int)
        word_ch= defaultdict(int)
        # s_=s.split()
        for i in range (len(s_)):
            word=s_[i]
            ch=pattern[i]
            if word in word_ch and ch in ch_word:
                if word_ch[word] != ch or ch_word[ch] != word:
                    return False
                # else:
                #     return False
            elif ch in ch_word or word in word_ch:
                return False
            else:
                word_ch[word] = ch
                ch_word[ch] = word
        return True
                


      


       
        