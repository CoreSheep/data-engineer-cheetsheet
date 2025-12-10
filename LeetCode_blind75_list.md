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
```

#### Product of Array Except Self
link: https://leetcode.com/problems/product-of-array-except-self/
#### Maximum Subarray
link: https://leetcode.com/problems/maximum-subarray/
#### Maximum Product Subarray
#### Find Minimum in Rotated Sorted Array
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