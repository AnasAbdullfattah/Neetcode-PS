class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # nlongn
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # result = 1
        # current_max = 1
        # nums.sort()

        # for i in range(1,n):
        #     if nums[i-1] == nums[i]:
        #         continue
        #     elif nums[i] == nums[i-1]+1:
        #         current_max = current_max+1
        #     else:
        #         current_max = 1
            
        #     if current_max > result:
        #         result = current_max
        # return result

        # n
        nums_set = set(nums)
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        max_cons = 0
        result = 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                max_cons = 1
                while (num + max_cons) in nums_set:
                    max_cons = max_cons + 1
            
            if max_cons > result:
                result = max_cons
        return result


x = Solution()
a = x.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(a)