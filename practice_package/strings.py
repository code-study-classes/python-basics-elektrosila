def extract_file_name(full_file_name: str) -> str:
    return full_file_name.split('/')[-1].split('.')[0]

def encrypt_sentence(sentence: str) -> str:
    even_chars = sentence[::2]
    odd_chars = sentence[1::2][::-1]
    return even_chars + odd_chars

def check_brackets(expression: str) -> int:
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i
            stack.pop()
    return -1 if stack else 0

def reverse_domain(domain: str) -> str:
    return '.'.join(domain.split('.')[::-1])

def count_vowel_groups(word: str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0
    in_group = False
    
    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count