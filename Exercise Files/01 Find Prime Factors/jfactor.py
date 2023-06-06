from cProfile import run


def get_prime_factors(N):
    N = x
    factors = list()
    divisor = 2
    while (divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1
    return factors


if __name__ == '__main__':
    run = True
    while (run == True):
        z = input("Enter your number to get prime factors or 'exit' to quit:")
        while (z == "exit"):
            run = False
            break
        else:
            x = int(z)
            print(get_prime_factors(x))
