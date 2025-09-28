from testcases import test_cases
from itertools import combinations

def three_sum_brute(nums,target):
    n = len(nums)
    unique_triplets = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==target:
                    unique_triplets.add(tuple(sorted([nums[i],nums[j],nums[k]])))
    
    return unique_triplets

if __name__ == "__main__":
    for idx, (nums, target, expected) in enumerate(test_cases):
        result = sorted([sorted(triplet) for triplet in three_sum_brute(nums, target)])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        print(f"Test case {idx+1}: {'PASS' if result == expected_sorted else 'FAIL'}")
        print(f"Input: {nums}, Target: {target}")
        print(f"Expected: {expected_sorted}")
        print(f"Got: {result}\n")
