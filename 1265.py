TT = int(input())

for _ in range(TT):
    money, division = map(int, input().split())
    total = 1

    candidiate = money // division
    left = money % division
    for i in range(division):
        if left:
            total *= (candidiate + 1)
            left -= 1
        else:
            total *= candidiate

    print("#{} {}".format(_ + 1, total))