class Solution:
    def isPowerOfTwo(self, n):
        # Base Case
        if n == 1:
            return True

        if n <= 0:
            return False

        if n % 2 != 0:
            return False

        # Recrusive Case
        return self.isPowerOfTwo(n//2)