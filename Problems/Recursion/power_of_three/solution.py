class Solution:
    def isPowerOfThree(self, n):
        # Base Case
        if n == 1:
            return True

        if n <= 0:
            return False

        if n % 3 != 0:
            return False

        # Recursive Case

        return self.isPowerOfThree(n//3)