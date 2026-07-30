'''
Maximum Average Subarray I
Approach1:

from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum = float("-inf")
    n = len(nums)
    for i in range(0,n-k+1):
        sub_sum = 0
        for j in range(i,k+i):
            sub_sum +=nums[j]
        max_sum = max(max_sum,sub_sum)
    return max_sum/k
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))
Approah 2:
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k

1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        win_sum = sum(arr[0:k])
        count = 0
        if(win_sum/k) >= threshold:
            count+=1
        n = len(arr)
        for i in range(n-k):
            win_sum = win_sum - arr[i] + arr[k+i]
            if (win_sum/k) >= threshold:
                count+=1
   
        return count
1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count
'''
