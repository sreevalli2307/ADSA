'''Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0  
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i


Two Sum II - Input Array Is Sorted

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left,right = 0,len(numbers)-1
    while left<right:
        s = numbers[left]+numbers[right]
        if s == target:
            return[left+1,right+1]
        elif s>target:
            right-=1
        else:
            left+=1
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))
'''