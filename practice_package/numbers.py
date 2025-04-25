def calculate_distance(x, y):
    return abs(y - x)

def calculate_segments(length_a, length_b):
    return length_a // length_b

def calculate_digit_sum(number):
   number = abs(number)  
   return sum(int(digit) for digit in str(number))

def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height

def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple



if __name__ == "__main__":
    print("Test calculate_distance:", calculate_distance(0, 5)) 
    print("Test calculate_segments:", calculate_segments(10, 3))  
    print("Test calculate_digit_sum:", calculate_digit_sum(47))  
    print("Test calculate_rect_area:", calculate_rect_area(0, 0, 5, 3))  
    print("Test round_to_multiple:", round_to_multiple(10, 3))  