from testcases import test_cases
'''
Time: O(n) where n is the length of the `nums` array
Space: O(1)
'''
def two_sum_two_pointer(nums, target):
    start,end = 0,len(nums)-1
    while start<end: 
        curr_sum = nums[start]+nums[end]
        if curr_sum>target: 
            end-=1
        elif curr_sum<target: 
            start+=1
        else:
            return [start,end]
    return []

if __name__ == "__main__":
    for nums, target in test_cases:
        result = two_sum_two_pointer(nums, target)
        print(f"Input: nums={nums}, target={target} => Output: {result}")