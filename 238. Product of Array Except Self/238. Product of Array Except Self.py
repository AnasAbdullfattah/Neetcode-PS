class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #nested for loop
        # result = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         result[i] = nums[j] * result[i]
        # return result

        #///////////////////////
        #pos suff
        n = len(nums) 
        pos = [1] * n
        pos[1] = nums[0]
        suf = [1] * n
        suf[len(nums) - 2] = nums[n - 1]
        result = [1] * n
        for i in range (2,(n)):
            pos[i] = pos[i-1] * nums[i-1]
        for i in range ((n) -3,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(n):
            result[i] = suf[i] * pos[i]
        return result

a = Solution()
x = a.productExceptSelf([1,2,3,4])    
# pos = 1[1,2,6]
# suf = [24,12,4]1
# Exprected [24,12,8,6]
print(x)