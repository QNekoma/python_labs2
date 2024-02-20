import math

for num in range(174457, 174505 + 1):
    divisors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    if len(divisors) == 2:
        divisors.sort()
        print(divisors[0], divisors[1])