from testcases import test_cases

def isalphanum(char):
    return char.isalnum()


def valid_palindrome(string):
    n = len(string)
    start,end = 0,n-1

    while end>start:
        if not isalphanum(string[start]):
            start+=1
            continue
        if not isalphanum(string[end]):
            end-=1
            continue
        if string[start]!=string[end]:
            return False
        start+=1
        end-=1
    return True



if __name__ == "__main__":
    for idx, (input_str, expected) in enumerate(test_cases):
        result = valid_palindrome(input_str)
        print(f"Test case {idx+1}: {'PASS' if result == expected else 'FAIL'}")
        print(f"Input: {repr(input_str)}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")