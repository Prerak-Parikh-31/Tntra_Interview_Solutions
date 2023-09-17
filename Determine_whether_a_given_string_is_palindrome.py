'''Determine whether a given string is palindrome
A string “madam” is a palindromic string because it reads the same forwards and backward.
Input: “anna”
Output: true

Input: “India”
Output: false'''
def is_palindrome(S: str) -> str:
    """
    Check if a string is a palindrome.

    Args:
        S (str): The input string.

    Returns:
        str: "Yes" if the string is a palindrome, "No" otherwise.
    """
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - i - 1]:
            return "No"
    return "Yes"

S1 = "anna"
print(is_palindrome(S1))

S2 = "India"
print(is_palindrome(S2))

