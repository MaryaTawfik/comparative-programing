class FrequencyTracker:

    def __init__(self):
        self.freq = {} 
        self.num = {}   

    def add(self, number: int) -> None:
        oldfrq = self.num.get(number, 0)
        newfrq = oldfrq + 1
        self.num[number] = newfrq

        if oldfrq > 0:
            self.freq[oldfrq] -= 1
        self.freq[newfrq] = self.freq.get(newfrq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.num or self.num[number] == 0:
            return
        oldfrq = self.num[number]
        newfrq = oldfrq - 1
        self.num[number] = newfrq

        self.freq[oldfrq] -= 1
        if newfrq > 0:
            self.freq[newfrq] = self.freq.get(newfrq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq.get(frequency, 0) > 0

        # freq=Counter(self.res)
        # ans= [True if count==frequency else False for count in freq.values()]
        # return  True in ans

        
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)