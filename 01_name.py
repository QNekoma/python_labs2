from itertools import product

letters = ['Т', 'И', 'М', 'О', 'Ф', 'Е', 'Й']
valid_codes = 0

for code in product(letters, repeat=5):
    if code.count('Й') <= 1 and 'ИЙ' not in code and code[1] != 'Й' and code[-1] != 'Й':
        valid_codes += 1

print(valid_codes)

