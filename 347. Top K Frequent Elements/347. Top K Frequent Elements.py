from heapq import heappop, heappush

class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

# the Dictionary/hashmap solution
        # my_dictionary = {}
        # for num in nums:
        #     if num in my_dictionary:
        #         my_dictionary[num] = my_dictionary[num]+1
        #     else:
        #         my_dictionary[num] = 1

        # x = dict(sorted(my_dictionary.items() , key=lambda t : t[1] , reverse=True))
        # result = list(x.keys())
        # result2 = []
        # for i in range(k):
        #     result2.append(result[i])

        # return list(result2)

        #///////////////////////////////
        #heap_sort
        my_dictionary = {}
        for num in nums:
            my_dictionary[num] = 1 + my_dictionary.get(num,0)
        heap = []
        for i, n in my_dictionary.items():
            heappush(heap,[n,i])
            if len(heap) > k:
                heappop(heap)
        print(heap)
        result = []
        while len(result) < k:  
            result.append(heappop(heap)[1])  
   
        return result  
        

a = Solution()
x = a.topKFrequent([6,6,1,2,2,34,5],2) 
print(x)