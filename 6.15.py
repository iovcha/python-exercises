Pi = 3
count = 0
multiplier = 0
while count < 5:
    multiplier += 2
    Pi = Pi + 4 / ((multiplier) * (multiplier + 1) * (multiplier + 2))
    multiplier += 2
    Pi = Pi - 4 / ((multiplier) * (multiplier + 1) * (multiplier + 2))
    print(Pi)
    count += 1
