# No starter code provided — write the full function yourself.
# Function name: to_roman
# Parameter: number (1 to 3999)
# Must return: the Roman numeral as a string

def to_roman(number):

    values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    result = ''

    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value
    
    return result

print(to_roman(1994))