class Solution:
    def isMonotonic(self, array: list) -> bool:
        is_increasing = True
        is_decreasing = True

        for i in range(1, len(array)):
            if array[i] > array[i-1]:
                is_decreasing = False
            if array[i] < array[i-1]:
                is_increasing = False

        return is_increasing or is_decreasing
    
Solution.isMonotonic(simple = [1,2,3,4])