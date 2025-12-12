## Blind 75 - Complete List
Blind 75 - Complete List
The famous list from a Meta engineer, organized by pattern:

### Arrays & Hashing (9) ✅

#### Two Sum ✅
- [Two Sum](https://leetcode.com/problems/two-sum/)  
-solution: hash table (seen)  
- space: O(n) - seen hash table  
- time: O(n) - one pass through the array  

#### Best Time to Buy and Sell Stock ✅  
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
- solution: two pointers (left and right) - left is the minimum price, right is the maximum price  
- space: O(1) - min_price and max_profit  
- time: O(n) - one pass through the array  

#### Contains Duplicate ✅
- [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)  
- solution: hash table (seen) - if the number is already in the hash table, return True  
- space: O(n) - seen hash table  
- time: O(n) - one pass through the array  
- note: use set() instead of hash table for better performance  
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

#### Product of Array Except Self ✅
- [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)  
- solution: prefix and suffix product  
- space: O(n) - answer array  
- time: O(n) - two passes through the array, prefix and suffix product  
- note: use prefix and suffix product to calculate the product of the array except self  
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
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)  
- solution: Kadane's Algorithm (dynamic programming)  
- space: O(1) - max_sum, current_sum  
- time: O(n) - one pass through the array  
- note: use Kadane's Algorithm to check if the current sum is greater than the current number, if it is, extend the current sum, if it is not, restart the current sum.  
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
- [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)  
- solution: Kadane's Algorithm (dynamic programming)  
- space: O(1) - max_product, min_product, max_product  
- time: O(n) - one pass through the array  
- note: A little different from the maximum subarray, because we need to consider the negative numbers. (save the min_product and max_product)  
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
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)  
solution: binary search<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: use binary search to find the minimum number in the rotated sorted array<br>
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
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
solution: binary search, find the sorted half and check if the target is in the sorted half<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: use binary search to find the target number in the rotated sorted array<br>
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
- [3Sum](https://leetcode.com/problems/3sum/)  
solution: 
    - sort the array<br>
    - fix one number and use two pointers to find the other two numbers<br>
    - skip the duplicate numbers<br>  
- time: O(n^2)<br>
- note: use two pointers to find the b + c = -a<br>
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
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
solution: two pointers<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use two pointers to check if the string is a palindrome from both sides<br>
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
- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  
solution: two pointers<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use two pointers to find the maximum area, pay attention to how to move the pointers<br>

#### 3Sum (also listed above) ✅ 
- [3Sum](https://leetcode.com/problems/3sum/)  
- solution: two pointers<br> (need to catch up later)


### Sliding Window (4) ✅
The core idea is to use a window to slide through the array, and use two pointers to keep track of the window. Move the right pointer to expand the window, and move the left pointer to shrink the window when a duplicate is found. Stop when the right pointer hits the end of the array.

#### Longest Substring Without Repeating Characters ✅
- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
solution: sliding window<br>
- space: O(1)<br>
- time: O(n)<br>
- note: use sliding window to find the longest substring without repeating characters<br>
1. version 1: use set to store the seen letters
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    # sliding window
    # Stop: when r hits the end
    # move l when meeting a repeated letter unless no repeated letters
    # expand right, shrink left when duplicate found
    if len(s) == 0 or len(s) == 1:
        return len(s)

    l, r = 0, 0
    seen = set()
    max_len = 0

    while r < len(s):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        r += 1
        max_len = max(max_len, r - l)
    return max_len
```

2. version 2: cleaner version
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    seen = {}
    max_len = 0

    for r in range(len(s)):
        while s[r] in seen:  # found duplicate
            seen.remove(s[l])  # shrink the left point of current window
            l += 1
        seen.add(s[r])  # add new char to the window
        r += 1  # move right pointer
        max_len = max(max_len, r - l)  # update max_len for each right pointer move
    return max_len
```

#### Longest Repeating Character Replacement ✅
- [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)  
- solution: sliding window<br>
- space: O(1) - count hash table<br>
- time: O(n)<br>
- note: when the window is valid, move the right pointer to expand the window, when the window is invalid, move the left pointer to shrink the window<br>
```python
def characterReplacement(self, s: str, k: int) -> int:
    # sliding window
    # use count to find the max_freq (the final character)
    # if the num of characters(need to be replaced) > k, move left, update the count
    # update the max_len
    count = {}
    l = 0
    max_len = 0
    max_freq = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_freq = max(count[s[r]], max_freq)

        # window invalid: too many characters to replace
        while (r - l + 1) - max_freq > k:  # shrink the window
            count[s[l]] -= 1
            l += 1
        max_len = max(r - l + 1, max_len)
    return max_len
```
#### Minimum Window Substring
- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  
- solution: sliding window<br>
- space: O(1)<br>
- time: O(n)<br>
```python
def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    from collections import Counter
    
    need = Counter(t)       # chars we need
    required = len(need)    # unique chars to satisfy
    have = 0                # unique chars satisfied
    
    window = {}
    l = 0
    result = ""
    min_len = float('inf')
    
    for r in range(len(s)):
        # Add right char to window
        c = s[r]
        window[c] = window.get(c, 0) + 1
        
        # Check if this char is now satisfied
        if c in need and window[c] == need[c]:
            have += 1
        
        # Shrink window while valid
        while have == required:
            # Update result if smaller
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                result = s[l:r+1]
            
            # Remove left char
            left_c = s[l]
            window[left_c] -= 1
            if left_c in need and window[left_c] < need[left_c]:
                have -= 1
            l += 1
    
    return result
```


#### Best Time to Buy and Sell Stock (revisited with window) ✅
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
- solution: sliding window<br>
- space: O(1)<br>
- time: O(n)<br>
- note: if you find a smaller buy price, update the buy price, and update the max profit<br>
```python
def maxProfit(self, prices: List[int]) -> int:
    # sliding window
    # expand and shrink
    l = 0
    max_profit = float('-inf')

    for r in range(len(prices)):  # expand the r
        if prices[l] < prices[r]:
            max_profit = max(prices[r] - prices[l], max_profit)
        else:
            l = r  # shrink the l (when you find smaller buy day)
    return max_profit if max_profit != float('-inf') elses 0
```


### Stack (1) ✅

#### Valid Parentheses
- [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)  
- solution: stack<br>
- space: O(n)<br>
- time: O(n)<br>
- note: use stack to check if the parentheses are valid<br>
```python
    def isValid(self, s: str) -> bool:
        # '(', '{' --> push
        # ')' --> pop to see if they match
        # stop: empty stack
        parentheses_dic = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        right_parentheses = [')', ']', '}']
        stack = []
        for c in s:
            if c in parentheses_dic:  # '(', '{', '[' --> push
                stack.append(parentheses_dic[c])
            elif c in right_parentheses:  # ')', ']', '}' --> pop to see if they match
                if not stack:  # if stack is empty
                    return False
                if stack and stack.pop() != c:  # if top stack element does not match the current parentheses
                    return False
        return not stack  # if there's still element in stack, return False, otherwise return True
```

### Binary Search (2) ✅

#### Find Minimum in Rotated Sorted Array ✅
- [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)  
- solution: binary search<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: keep m as candidate, and compare it with the end of the array to find the minimum number<br>
```python
def findMin(self, nums: List[int]) -> int:
    # binary search
    # the minimum is always on the unsorted half
    # update l, r, m

    l, r = 0, len(nums) - 1
    minimum = float('inf')
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:  # go to the right unsorted half to find the minimum
            l = m + 1
        else:
            r = m  # keep m as candidate when jump to the left half
    return nums[l]
```

#### Search in Rotated Sorted Array ✅
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)  
- solution: binary search<br>
- space: O(1)<br>
- time: O(log n)<br>
- note: use binary search to find the target number in the rotated sorted array<br>
```python
def search(self, nums: List[int], target: int) -> int:
    # same as find the minimum in rotated sorted array
    # find which half is sorted half, then check if the target is in that half
    # otherwise go check the other half
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        # left half is sorted
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        # right half is sorted
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

```


### Linked List (6) ✅

#### Reverse Linked List ✅
- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)  
- solution: iterative<br>
- space: O(1)<br>
- time: O(n)<br>
- note: draw the linked list to understand the process<br>
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre
```

#### Merge Two Sorted Lists ✅
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)  
- solution: iterative<br>
- space: O(1)<br>
- time: O(n)<br><br>
- note: use dummy node to simplify the code, two pointers moving through the lists and attach the remaining list<br>

```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # three points + dummy node
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next

        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:  # attach the remaining list
        curr.next = list1
    if list2:
        curr.next = list2

    return dummy.next
```


#### Linked List Cycle
#### Reorder List ✅
- [Reorder List](https://leetcode.com/problems/reorder-list/)  
- solution: two pointers<br>
- space: O(1)<br>
- time: O(n)<br>
- note: find the middle of the list and reverse the second half, then merge the two lists<br>
```python
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    1. find the middle
    2. reverse the second half
    3. merge two half
    """
    # 1. find the middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # 2. reverse the second half
    second = slow.next  # start from the second half
    slow.next = None  # cut the first half
    pre = None
    cur = second
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    
    # 3. merge two halves
    first, second = head, pre
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
```
#### Remove Nth Node From End of List
#### Merge K Sorted Lists


### Trees (11)

#### Invert Binary Tree
#### Maximum Depth of Binary Tree
#### Same Tree
#### Subtree of Another Tree ✅
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