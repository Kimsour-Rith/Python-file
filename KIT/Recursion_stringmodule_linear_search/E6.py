import string

def find_sum_of_digit(n):
    sum_of_digit = 0
    non_numbers = []
    for i in n:
        if i.isdigit():
            sum_of_digit += int(i)
    print("Sum of the digit:", sum_of_digit)

    for i in n:
        if i not in string.digits:
            non_numbers.append(i)
    print("The following are not numbers and can't be converted...", non_numbers)


find_sum_of_digit("1312abcd")
