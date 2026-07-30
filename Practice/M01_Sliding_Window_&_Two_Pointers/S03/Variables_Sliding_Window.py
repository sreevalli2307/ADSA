
'''209. #Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        min_len = float("inf")

        for right in range(n):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))

713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left,count = 0,0
        p=1
        for right in range(len(nums)):
            p *= nums[right]
            while p>=k:
                p //= nums[left]
                left+=1
            count +=(right-left+1)
        return count
        
904. Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = {}
        ans = 0

        for right, f in (fruits):
            count[f] = count.get(f, 0) + 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)

        return ans
'''