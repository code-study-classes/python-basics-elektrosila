def check_between_numbers(A, B, C):
    return A < B < C or C < B < A

def check_odd_three(number):
    return 100 <= abs(number) <= 999 and number % 2 != 0

def check_unique_digits(number):
    number = abs(number) 
    if 100 <= number <= 999:
        digits = str(number)
        return len(set(digits)) == len(digits)
    return False

def check_palindrome_number(number):
    return str(abs(number)) == str(abs(number))[::-1]

def check_ascending_digits(number):
    number = abs(number)  
    if 100 <= number <= 999:
        digits = str(number)
        return digits == ''.join(sorted(digits))
    return False