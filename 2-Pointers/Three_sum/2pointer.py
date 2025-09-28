from testcases import test_cases

def twopairsum(nums,target):
    n = len(nums)
    pairs = []
    start,end = 0,n-1
    while start<end:
        curr_sum = nums[start]+nums[end]
        if curr_sum==target:
            pairs.append([start,end])
            start+=1
            end-=1
            while start < end and nums[start] == nums[start-1]:
                start += 1
            while start < end and nums[end] == nums[end+1]:
                end -= 1
        elif curr_sum>target:
            end-=1
        else:
            start+=1
    return pairs
        
def three_sum_two_pointer(nums, target):
    n = len(nums)
    nums.sort()
    unique_triplets = set()
    for a in range(n):  
        if a>0 and nums[a]==nums[a-1]:
            continue
        else:
             for b,c in twopairsum(nums[a+1:],target-nums[a]):
                 unique_triplets.add(tuple(sorted([nums[a],nums[b+a+1],nums[c+a+1]])))

            
    return [list(triplet) for triplet in unique_triplets]
if __name__ == "__main__":
    for idx, (nums, target, expected) in enumerate(test_cases):
        result = sorted([sorted(triplet) for triplet in three_sum_two_pointer(nums, target)])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        print(f"Test case {idx+1}: {'PASS' if result == expected_sorted else 'FAIL'}")
        print(f"Input: {nums}, Target: {target}")
        print(f"Expected: {expected_sorted}")
        print(f"Got: {result}\n")
