import math

letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

output_list = list()
e = 13
n = 35
phi = 24
input_data1 = ""
input_string = "16.1.18.1.14.10.1.25"
numbers_list = input_string.split(".")
numbers = [int(num) for num in numbers_list]

# Find the modular multiplicative inverse of e modulo phi
d = pow(e, -1, phi)

for val in numbers:
    PT = pow(val, d, n)
    for letter, number in letter_to_number.items():
        if number == PT:
            input_data1 += letter

print(input_data1)
