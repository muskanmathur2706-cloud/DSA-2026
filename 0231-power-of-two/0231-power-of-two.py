class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        ans = 1
        while ans < n:
            ans *= 2

        return ans == n
