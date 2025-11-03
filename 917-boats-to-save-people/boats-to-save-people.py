class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # pair lightest with heaviest
            right -= 1
            boats += 1  # one boat used

        return boats
