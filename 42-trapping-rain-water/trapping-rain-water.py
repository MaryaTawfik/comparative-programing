class Solution:
    def trap(self, height: List[int]) -> int:
        right = []
        left = []

        left_max = height[0]

        for i in range(len(height)):
            left_max = max(left_max, height[i])
            left.append(left_max)

        print(left)

        max_right = height[-1]

        for j in range(len(height)-1, -1, -1):
            max_right = max(max_right, height[j])
            right.append(max_right)

        right.reverse()

        print(right)

        ans = 0

        for i in range(len(height)):
            x = min(left[i], right[i])
            ans += x - height[i]

        return ans