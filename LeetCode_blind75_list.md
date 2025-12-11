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


#### Maximum Subarray ✅
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


#### Find Minimum in Rotated Sorted Array ✅
link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/<br>
solution: binary search<br>
space: O(1)<br>
time: O(log n)<br>
note: use binary search to find the minimum number in the rotated sorted array<br>
```python
def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if  nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
        return nums[l]
```

#### Search in Rotated Sorted Array ✅
link: https://leetcode.com/problems/search-in-rotated-sorted-array/<br>
solution: binary search, find the sorted half and check if the target is in the sorted half<br>
space: O(1)<br>
time: O(log n)<br>
note: use binary search to find the target number in the rotated sorted array<br>
```python
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        if nums[m] == target:
            return m
        
        # Left half is sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1  # target in left half
            else:
                l = m + 1  # target in right half
        
        # Right half is sorted
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1  # target in right half
            else:
                r = m - 1  # target in left half
    return -1
    ```

#### 3Sum ✅
link: https://leetcode.com/problems/3sum/<br>
solution: 
    - sort the array<br>
    - fix one number and use two pointers to find the other two numbers<br>
    - skip the duplicate numbers<br>
space: O(1)<br>
time: O(n^2)<br>
note: use two pointers to find the b + c = -a<br>
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining two numbers
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            
            while l < r:
                total = nums[l] + nums[r]
                
                if total == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        return result
```

### Two Pointers (3) ✅

#### Valid Palindrome ✅
link: https://leetcode.com/problems/valid-palindrome/<br>
solution: two pointers<br>
space: O(1)<br>
time: O(n)<br>
note: use two pointers to check if the string is a palindrome from both sides<br>
```python
def isPalindrome(self, s: str) -> bool:
    # 'a'.isalnum(), 'a'.isalpha(), '4'.isdigit()
    # remove non-alphanumeric characters and convert them to lowercase letters
    s_new = "".join([c for c in s if c.isalnum()]).lower()
    
    # two points
    l, r = 0, len(s_new) - 1
    while l < r:
        if s_new[l] != s_new[r]:
            return False
        l += 1
        r -= 1
    return True
```

#### Container With Most Water ✅
link: https://leetcode.com/problems/container-with-most-water/<br>
solution: two pointers<br>
space: O(1)<br>
time: O(n)<br>
note: use two pointers to find the maximum area<br>
```python
def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0
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