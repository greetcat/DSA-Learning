# Each test case: (input_array, expected_output)
# Expected output = maximum water that can be contained

test_cases = [
    # Basic case from LeetCode
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),

    # Two bars only
    ([1, 1], 1),
    ([1, 2], 1),
    ([2, 1], 1),

    # Increasing heights
    ([1, 2, 3, 4, 5], 6),  # Between 2 and 5 → min(2,5)*(4-1)=6

    # Decreasing heights
    ([5, 4, 3, 2, 1], 6),  # Between 5 and 2 → min(2,5)*(3-0)=6

    # Multiple equal heights
    ([3, 3, 3, 3], 9),  # Between first and last → 3*(3)=9

    # Edge cases
    ([], 0),          # no bars
    ([5], 0),         # only one bar
    ([0, 0, 0], 0),   # all zero heights

    # Random example
    ([1, 3, 2, 5, 25, 24, 5], 24),  # Between heights 25 and 5 (index 4 and 6)
]
