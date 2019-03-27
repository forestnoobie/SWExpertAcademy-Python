TT = int(input())

for _ in range(TT):
    N, M = map(int, input().split())

    print("#{} {} {}".format(_ + 1, 2 * M - N, N - M))