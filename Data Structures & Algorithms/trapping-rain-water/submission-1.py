class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [], []
        pre, post, sum, vol = 0, 0, 0, 0
        for i in range(len(height)):
            prefix.append(pre)
            pre = max(pre, height[i])

        for i in range(len(height)-1, -1, -1):
            suffix.append(post)
            post = max(post, height[i])

        for i in range(len(height)):
            vol = min(prefix[i], suffix[-i]) - height[i]
            if vol > 0:
                sum += vol
        return sum