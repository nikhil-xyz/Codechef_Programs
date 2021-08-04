from math import ceil
powers = {}
MOD = 1000000007
def power_calculation(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        powers[exp] = base
        return base % MOD

    if exp in powers.keys():
        return powers[exp]
    else:
        result = power_calculation(base, int(exp/2))
        result *= result

        if (exp % 2) == 0:
            powers[exp] = result % MOD
            return result % MOD
        else:
            powers[exp] = ((base % MOD) * result) % MOD
            return ((base % MOD) * result) % MOD

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    result = power_calculation(2, n) - 1
    powers.clear()
    result = power_calculation(result, m)
    powers.clear()
    print(result)
