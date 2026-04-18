class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 0
            my_dict[num] += 1

        # short the dict based on the value
        print(my_dict.items())
        print(type(my_dict.items()))
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x:x[1], reverse=True)[:k])

        result = []
        for key in sorted_dict.keys():
            result.append(key)
        return result