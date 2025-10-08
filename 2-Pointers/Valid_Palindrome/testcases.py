# Each test case: (input_string, expected_output)
# expected_output = True if palindrome (case-sensitive, alphanumeric only), else False

test_cases = [
    # Simple palindromes
    ("abba", True),
    ("aabaa", True),

    # Case-sensitive examples
    ("Aa", False),         # 'A' != 'a'
    ("Madam", False),      # M != m

    # Includes spaces and punctuation
    ("A man, a plan, a canal: Panama", False),  # case-sensitive
    ("No lemon, no melon", False),              # case-sensitive
    ("ab@#a", True),                            # special chars ignored

    # Numbers
    ("12321", True),
    ("123321", True),
    ("123421", False),

    # Mix of letters and numbers
    ("1a2a1", True),
    ("1A2a1", False),

    # Edge cases
    ("", True),             # empty string is palindrome
    ("!!!", True),          # only non-alphanum = empty string → palindrome
    ("a", True),            # single char
    ("ab", False),          # two chars different
]
