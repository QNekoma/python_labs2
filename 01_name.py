letters = ['Т', 'И', 'М', 'О', 'Ф', 'Е', 'Й']
valid_codes = 0

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                for letter5 in letters:
                    code = letter1 + letter2 + letter3 + letter4 + letter5
                    if code.count('Й') <= 1 and 'ИЙ' not in code and code[1] != 'Й' and code[-1] != 'Й':
                        valid_codes += 1

print(valid_codes)
