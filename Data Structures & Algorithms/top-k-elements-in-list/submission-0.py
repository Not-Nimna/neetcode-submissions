class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for val in nums:
            if val not in count_dict.keys():
                count_dict[val] = 1
            else:
                count_dict[val] += 1

        sort_arr = []
        for key, val in count_dict.items():
            sort_arr.append([val,key])
        sort_arr.sort(reverse=True)

        ret_arr = []

        for i in range(k):
            ret_arr.append(sort_arr[i][1])


        return ret_arr