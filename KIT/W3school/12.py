def isPalindrome(string):
    left_pos = 0
    lenght_string = len(string)
    right_pos =lenght_string - 1

    while right_pos >= left_pos:
        if string[left_pos] != string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(isPalindrome('aza'))