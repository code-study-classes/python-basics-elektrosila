def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total

def count_vowel_triplets(text):
    vowels = "aeiouyAEIOUY"  
    count = 0
    for i in range(len(text) - 2):
        if text[i] in vowels and text[i+1] in vowels and text[i+2] in vowels:
            count += 1
    return count

def find_fibonacci_index(number):
    if number < 1:
        return -1
    a, b = 1, 1
    index = 2 if number > 1 else 1
    if number == 1:
        return 1  
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for char in string[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)