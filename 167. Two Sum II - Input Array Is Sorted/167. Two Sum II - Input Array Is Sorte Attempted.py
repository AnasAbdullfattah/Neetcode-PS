class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while(left < right):

            if (numbers[left] + numbers[right]) > target:
                right = right - 1

            elif (numbers[left] + numbers[right]) < target:
                left = left + 1

            else:
                return [left+1,right+1]
        
        return []


x = Solution()
a = x.twoSum([0,0,1], 0)
print(a)