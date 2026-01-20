# Two Sum - Hash Map Solution

## Problem
Find two numbers in an array that add up to a target value. Return their indices.

## Core Idea
Use a hash map to store numbers we've seen. For each number, check if its complement (target - current) already exists in the map.

## The Code
```python
def twoSum(nums: list[int], target: int):
    l = {}
    for i, v in enumerate(nums):
        diff = target - nums[i]
        if diff in l:
            return [l[diff], i]
        l[v] = i
    return []
```

## How It Works
1. **Loop through array** with index and value
2. **Calculate complement**: `diff = target - current_number`
3. **Check if complement exists** in hash map
   - If YES → return `[stored_index, current_index]`
   - If NO → store `map[current_number] = current_index`

## Example Trace
`nums = [2, 7, 11, 15]`, `target = 9`

| i | v | diff | Hash Map Before | Action |
|---|---|------|----------------|--------|
| 0 | 2 | 7 | `{}` | Store: `{2: 0}` |
| 1 | 7 | 2 | `{2: 0}` | Found! Return `[0, 1]` |

## Why This Works
- **O(1) lookup**: Hash map check is constant time
- **Single pass**: Only iterate once through array
- **Store as we go**: First number is already saved when we encounter its pair

## Complexity
- **Time**: O(n) - one loop through array
- **Space**: O(n) - worst case store all elements

## Key Insight
Don't check all pairs (O(n²)). Instead, ask: "Have I already seen the number I need?" This transforms a quadratic problem into linear time.
