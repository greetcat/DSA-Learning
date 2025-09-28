from testcases import test_cases

'''
Time: O(n^2) where n is the length of the `nums` array
Space: O(1)
'''
def two_sum_brute(nums, target):
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target: 
                # print(f"Adding {nums[i]} and {nums[j]}")
                return [i,j]
    return []
if __name__ == "__main__":
    for nums, target in test_cases:
        result = two_sum_brute(nums, target)
        print(f"Input: nums={nums}, target={target} => Output: {result}")