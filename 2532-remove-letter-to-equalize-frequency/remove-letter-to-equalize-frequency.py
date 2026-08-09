from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq_count = Counter(freq.values())
        if len(freq_count) == 1:
            frequency = list(freq_count.keys())[0]
            number_of_characters = list(freq_count.values())[0]

            return frequency == 1 or number_of_characters == 1
        if len(freq_count) > 2:
            return False

        frequencies = list(freq_count.keys())
        counts = list(freq_count.values())

        f1, f2 = frequencies
        c1, c2 = counts
        if f1 == 1 and c1 == 1:
            return True

        if f2 == 1 and c2 == 1:
            return True
        if f1 == f2 + 1 and c1 == 1:
            return True

        if f2 == f1 + 1 and c2 == 1:
            return True

        return False