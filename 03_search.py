for i in range(174457, 174506):
    divisors = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if j not in divisors:
                divisors.append(j)
            if i // j not in divisors:
                divisors.append(i // j)
    divisors.sort()
    if len(divisors) == 2:
        print(divisors[0], divisors[1])
