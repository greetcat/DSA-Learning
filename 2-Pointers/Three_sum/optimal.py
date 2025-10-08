from testcases import test_cases

def twopairsum(nums,target):
    start,end = 0,len(nums)-1
    pairs = []
    while end>start:
        summation = nums[end]+nums[start]
        if summation==target:
            pairs.append((nums[start],nums[end]))
            start+=1
            end-=1
            while end>start and nums[start]==nums[start-1]:
                start+=1
            while end>start and nums[end]==nums[end+1]:
                end-=1
        elif summation>target:
            end-=1
        else:
            start+=1
    return pairs
        
def three_sum_two_pointer(nums, target):
    n = len(nums)
    nums.sort()
    result = []
    for a in range(n): 
        if a>0 and nums[a]==nums[a-1]:
            continue
        pairs = twopairsum(nums[a+1:], target-nums[a])
        for b,c in pairs:
            result.append((nums[a],b,c))
    return result

    
if __name__ == "__main__":
    for idx, (nums, target, expected) in enumerate(test_cases):
        result = sorted([sorted(triplet) for triplet in three_sum_two_pointer(nums, target)])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        print(f"Test case {idx+1}: {'PASS' if result == expected_sorted else 'FAIL'}")
        print(f"Input: {nums}, Target: {target}")
        print(f"Expected: {expected_sorted}")
        print(f"Got: {result}\n")
