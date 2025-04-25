
def is_weekend(day):
    """Определяет, является ли день выходным."""
    if day == 6 or day == 7:
        return True
    return False


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.1, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    return 0

def describe_number(n):
    if n == 0:
        return "четное однозначное число"
    if n < 1 or n > 999:
        return "Invalid number"
    even_or_odd = "четное" if n % 2 == 0 else "нечетное"
    if n < 10:
        return f"{even_or_odd} однозначное число"
    elif n < 100:
        return f"{even_or_odd} двузначное число"
    return f"{even_or_odd} трехзначное число"

def convert_to_meters(unitNumber, lengthInUnits):
    """Конвертирует длину в указанных единицах в метры."""
    if unitNumber == 1:
        return lengthInUnits * 0.1
    elif unitNumber == 2:
        return lengthInUnits * 1000
    elif unitNumber == 3:
        return lengthInUnits
    elif unitNumber == 4:
        return lengthInUnits * 0.001
    elif unitNumber == 5:
        return lengthInUnits * 0.01
    return 0


def describe_age(age):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    
    if age == 1:
        return "один год"
    
    if age == 2:
        return "два года"
    
    if age == 3 or age == 4:
        return f"{ones[age]} года"
    
    if age in range(10, 20):
        return f"{teens[age-10]} лет"
    
    hundreds_part = hundreds[age // 100]
    tens_part = tens[(age % 100) // 10]
    ones_part = ones[age % 10]
    
    if age % 10 == 1 and age % 100 != 11:
        ones_part = "один"
    elif age % 10 == 2 and age % 100 != 12:
        ones_part = "два"
    
    age_in_words = " ".join(filter(None, [hundreds_part, tens_part, ones_part])).strip()
    
  
    if age % 10 == 1 and age % 100 != 11:
        return age_in_words + " год"
    elif age % 10 in [2, 3, 4] and not (age % 100 in [12, 13, 14]):
        return age_in_words + " года"
    else:
        return age_in_words + " лет"