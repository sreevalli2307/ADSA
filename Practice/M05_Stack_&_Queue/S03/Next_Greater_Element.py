#496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        greater_ele = {}
        stack = []
        for num in nums2:
            while stack and stack[-1]<num:
                greater_ele[stack.pop()] = num
            stack.append(num)
        while stack:
            greater_ele[stack.pop()] = -1
        return[greater_ele[num] for num in nums1]
#method 2
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        stack = []
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <=nums2[i]:
                stack.pop()
            d[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])
        res =[]
        for ele in nums1:
            res.append(d[ele])
        return res
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))