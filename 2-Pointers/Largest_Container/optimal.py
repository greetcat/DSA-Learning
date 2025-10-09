from testcases import test_cases

def water_containter_optimal(array):
    max_vol = 0 
    n = len(array)
    start,end = 0,n-1
    while end>start:
        curr_vol = min(array[start],array[end])*(end-start)
        max_vol = max(curr_vol,max_vol)
        if array[start]>array[end]:
            end-=1
        else:
            start+=1
    
    return max_vol



if __name__ == "__main__":
    for idx, (input_arr, expected) in enumerate(test_cases):
        result = water_containter_optimal(input_arr)
        print(f"Test case {idx+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"Input: {input_arr}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")