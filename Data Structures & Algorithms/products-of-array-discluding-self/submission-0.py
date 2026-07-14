class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        big_val = 1
        zero_cnt = 0
        for val in nums:
            
            if val == 0:
                zero_cnt +=1
            else:
                big_val *= val


        if zero_cnt > 1:
            ret_arr = [0]* len(nums)
            return ret_arr

        ret_arr = []
        for val in nums: 
            
            if val == 0:
                ret_arr.append(big_val)
            else:
                if zero_cnt == 1:
                    ret_arr.append(0)
                else:
                    ret_arr.append(big_val//val)

        return ret_arr