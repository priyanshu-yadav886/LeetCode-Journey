# Monotonic Array

Link: https://leetcode.com/problems/monotonic-array/

## Problem

Given an integer array, return true if the array is monotonic, otherwise false.

An array is:

- Monotonic increasing → nums[i] <= nums[i+1]
- Monotonic decreasing → nums[i] >= nums[i+1]

## Intuition

A valid monotonic array must follow only ONE direction:

- Either entirely non-decreasing
- Or entirely non-increasing

If it switches direction even once → not monotonic.

## Approach

Track the direction of the array:

- Initialize two flags:
  - is_increasing = True
  - is_decreasing = True

Traverse the array:

- If nums[i] < nums[i-1] → not increasing
- If nums[i] > nums[i-1] → not decreasing

At the end:

- If either flag is True → array is monotonic

## Complexity

Time: O(n)
Space: O(1)

## Edge Cases

- Single element → always monotonic
- All elements same → monotonic
- Large negatives/positives → no issue

## Mistakes

- Confusing strictly increasing vs non-decreasing
- Not handling equal elements correctly
- Overcomplicating with sorting (unnecessary)

## Example

Input:
[1, 2, 2, 3]

Output:
True

Input:
[1, 3, 2]

Output:
False
