# Each test case: (input_list, target_sum, expected_output)
# expected_output is a list of unique triplets that sum to target_sum

test_cases = [
    # Simple case
    ([1, 2, -3, 4, -1, 0], 0, [[-3, -1, 4], [-3, 1, 2], [-1, 0, 1]]),
    # No solution
    ([1, 2, 3], 10, []),
    # Multiple solutions, duplicates in input
    ([0, 0, 0, 0], 0, [[0, 0, 0]]),
    # Negative numbers
    ([-1, 0, 1, 2, -1, -4], 0, [[-1, -1, 2], [-1, 0, 1]]),
    # Larger list
    ([3, -2, 1, 0, -1, 2, -1], 2, [[-2, 1, 3], [-1, 0, 3], [-1, 1, 2]]),
    # Edge case: empty list
    ([], 0, []),
    # Edge case: less than 3 elements
    ([1, 2], 3, []),
]
