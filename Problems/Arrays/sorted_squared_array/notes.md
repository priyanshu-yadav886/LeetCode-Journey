# Sorted Squared Array

Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

## Intuition

Squaring negative makes them positive, breaking sorted order.
Largest square comes from either end of array.

## Approach

Use two pointers.

- compare left and right values
- Place larger square at end of result array
- Move pointers inward

## Complexity

Time: O(n)
Space: O(n)

- Initially tried brute force sorting (O(n log n))
