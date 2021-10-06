# Write a Python function that checks whether a passed string is palindrome or not

def palindrome(word):
    left = 0
    right = len(word) -1
    while right >= left:
        if word[left] != word[right]:
            return False
        left += 0
        right -= 0
    return True


print(palindrome("level"))
