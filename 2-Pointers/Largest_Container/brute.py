from testcases import test_cases

def brute_force_largest_container(array):
    max_vol = 0
    n = len(array)
    for i in range(n):
        for j in range(i+1,n):
            curr_vol = min(array[i],array[j])*(j-i)
            max_vol = max(max_vol,curr_vol)
    return max_vol



if __name__ == "__main__":
    for idx, (input_arr, expected) in enumerate(test_cases):
        result = brute_force_largest_container(input_arr)
        print(f"Test case {idx+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"Input: {input_arr}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")