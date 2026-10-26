class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # the n^2 solution
        # for for
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]

        # --------------------
        #hashmap #1
        # my_dictionary = {}
        
        # for i in range(len(nums)):
        #     my_dictionary[nums[i]] = i

        # for i in range(len(nums)):
        #     diffrence = target - nums[i]
        #     if diffrence in my_dictionary and my_dictionary[diffrence] != i:
        #         return [i,my_dictionary[diffrence]]


        #hashmap #2
        my_dictionary = {}
    
        for i in range(len(nums)):
            diffrence = target - nums[i]  
            if (diffrence in my_dictionary):
                return [i,my_dictionary[diffrence]]
            else:
                my_dictionary[nums[i]] = i