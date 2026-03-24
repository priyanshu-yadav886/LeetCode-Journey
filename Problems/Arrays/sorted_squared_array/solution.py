class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        i, j = 0, n-1
        result = [0]*n

        for k in reversed(range(n)):
            if nums[i]**2 > nums[j]**2:
                result[k] = nums[i]**2
                i += 1

            else:
                result[k] = nums[j]**2
                j -= 1

        return result