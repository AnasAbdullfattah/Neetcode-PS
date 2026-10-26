class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # /////////////////////////////

        # a = {}

        # for num in nums:
        #     if num in a:
        #         a[num] = a[num] + 1
        #     else:
        #         a[num] = 1
        
        # for value in a.values():
        #     if value > 1:
        #         return True
        # return False

        # ///////////////

        # a = set()

        # for num in nums:
        #     if num in a:
        #         return True
        #     else:
        #         a.add(num)
        # return False
# ///////////////////
        # if len(set(nums)) < len(nums):
        #     return True
        # else:
        #     return False 

        return len(set(nums)) != len(nums)