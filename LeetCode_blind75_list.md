## Blind 75 - Complete List
Blind 75 - Complete List
The famous list from a Meta engineer, organized by pattern:

### Arrays & Hashing (9) ✅

#### Two Sum ✅
link: https://leetcode.com/problems/two-sum/
solution: hash table (seen)
space: O(n) - seen hash table
time: O(n) - one pass through the array

#### Best Time to Buy and Sell Stock ✅
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
solution: two pointers (left and right) - left is the minimum price, right is the maximum price
space: O(1) - min_price and max_profit
time: O(n) - one pass through the array

#### Contains Duplicate ✅
link: https://leetcode.com/problems/contains-duplicate/
solution: hash table (seen) - if the number is already in the hash table, return True
space: O(n) - seen hash table
time: O(n) - one pass through the array
note: use set() instead of hash table for better performance
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False

# initialize the seen set
seen = set()
seen = {1, 2, 3, 4, 5}
seen = set([1, 2, 3, 4, 5])

# add, remove, check if in set
seen.add(6)
seen.remove(1)
if 2 in seen:
    print("2 is in the set")
else:
    print("2 is not in the set")
```s

#### Product of Array Except Self ✅
link: https://leetcode.com/problems/product-of-array-except-self/
solution: prefix and suffix product
space: O(n) - answer array
time: O(n) - two passes through the array, prefix and suffix product
note: use prefix and suffix product to calculate the product of the array except self
```python
 def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix_prod = 1  # the prefix product of all  previous elements
        for i in range(len(nums)):
            answer[i] *= prefix_prod  # update for each prefix product
            prefix_prod *= nums[i]s

        suffix_prod = 1  # the suffix product of all previous element from back to front
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix_prod  # update for each suffix product
            suffix_prod *= nums[i]  # the answer should be prefix product * suffix product
        return answer
```


#### Maximum Subarray
link: https://leetcode.com/problems/maximum-subarray/
solution: Kadane's Algorithm (dynamic programming)
space: O(1) - max_sum, current_sum
time: O(n) - one pass through the array
note: use Kadane's Algorithm to check if the current sum is greater than the current number, if it is, extend the current sum, if it is not, restart the current sum.
```python
def maxSubArray(self, nums: List[int]) -> int:
    cursum = nums[0]
    maxsum = nums[0]

    for num in nums[1: ]:
        cursum = max(num, num + cursum)  # extend or restart?
        maxsum = max(maxsum, cursum)  # update for the global maxsum
    return maxsum
```

#### Maximum Product Subarray ✅
link: https://leetcode.com/problems/maximum-product-subarray/
solution: Kadane's Algorithm (dynamic programming)
space: O(1) - max_product, min_product, max_product
time: O(n) - one pass through the array
note: A little different from the maximum subarray, because we need to consider the negative numbers. (save the min_product and max_product)
```python
def maxProduct(self, nums: List[int]) -> int:
    cur_min = nums[0]
    cur_max = nums[0]
    max_prod = nums[0]

    for num in nums[1: ]:
        candidates = {num, cur_min * num, cur_max * num}
        cur_min = min(candidates) 
        # The reason that we save cur_min is that maybe later
        # the cur_min * num could be the current largest
        cur_max = max(candidates)
        max_prod = max(max_prod, cur_max)
    return max_prod
```


#### Find Minimum in Rotated Sorted Array
link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
solution: binary search
space: O(1) - left, right, mid
time: O(log n) - one pass through the array
note: use binary search to find the minimum number in the rotated sorted array

#### Search in Rotated Sorted Array
#### 3Sum


### Two Pointers (3) ✅

#### Valid Palindrome
#### Container With Most Water
#### 3Sum (also listed above)

### Sliding Window (4) ✅

#### Longest Substring Without Repeating Characters
#### Longest Repeating Character Replacement
#### Minimum Window Substring
#### Best Time to Buy and Sell Stock (revisited with window)

### Stack (1) ✅

#### Valid Parentheses

### Binary Search (2) ✅

#### Find Minimum in Rotated Sorted Array
#### Search in Rotated Sorted Array

### Linked List (6) ✅

#### Reverse Linked List
#### Merge Two Sorted Lists
#### Linked List Cycle
#### Reorder List
#### Remove Nth Node From End of List
#### Merge K Sorted Lists

### Trees (11)

#### Invert Binary Tree
#### Maximum Depth of Binary Tree
#### Same Tree
#### Subtree of Another Tree
#### Lowest Common Ancestor of BST
#### Binary Tree Level Order Traversal
#### Validate Binary Search Tree
#### Kth Smallest Element in BST
#### Construct Binary Tree from Preorder and Inorder
#### Binary Tree Maximum Path Sum
#### Serialize and Deserialize Binary Tree

### Tries (3)

#### Implement Trie (Prefix Tree)
#### Design Add and Search Words Data Structure
#### Word Search II

### Heap / Priority Queue (3)

#### Merge K Sorted Lists
#### Top K Frequent Elements
#### Find Median from Data Stream

### Backtracking (2)

#### Combination Sum
#### Word Search

### Graphs (8)

#### Number of Islands
#### Clone Graph
#### Pacific Atlantic Water Flow
#### Course Schedule
#### Course Schedule II
#### Number of Connected Components (premium)
#### Graph Valid Tree (premium)
#### Alien Dictionary (premium)

### Dynamic Programming (11)

#### Climbing Stairs
#### Coin Change
#### Longest Increasing Subsequence
#### Longest Common Subsequence
#### Word Break
#### Combination Sum IV
#### House Robber
#### House Robber II
#### Decode Ways
#### Unique Paths
#### Jump Game

### 1-D DP (additional)

#### Maximum Product Subarray
#### Partition Equal Subset Sum

### Intervals (5)

#### Insert Interval
#### Merge Intervals
#### Non-overlapping Intervals
#### Meeting Rooms (premium)
#### Meeting Rooms II (premium)

### Greedy (2)

#### Maximum Subarray
#### Jump Game

### Math & Geometry (3)

#### Rotate Image    
#### Spiral Matrix
#### Set Matrix Zeroes

### Bit Manipulation (5)    

#### Number of 1 Bits
#### Counting Bits
#### Reverse Bits
#### Missing Number
#### Sum of Two Integers