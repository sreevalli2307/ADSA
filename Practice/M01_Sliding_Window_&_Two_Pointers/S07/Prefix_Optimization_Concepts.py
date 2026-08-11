'''1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        t = 0
        for i in nums:
            t+=i
            res.append(t)
        return res
        

nums = [1,2,3,4]
res = [0]*(len(nums))
for i in range(len(nums)):
    curr_sum = 0 
    for j in range(0,i+1):
        curr_sum +=nums[j]
    res[i] = curr_sum
print(res)

1732
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr_alt = 0
        for g in gain:
            curr_alt += g
            max_alt = max(max_alt,curr_alt)
        return max_alt

1991
class Solution:

  def findMiddleIndex(self, nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
      if left_sum == total_sum - left_sum - num:
        return i
      left_sum += num

    return -1

724


class Solution:

  def pivotIndex(self, nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
      if left_sum == total_sum - left_sum - num:
        return i
      left_sum += num

    return -1

'''