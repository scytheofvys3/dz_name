# === DZ 41 Декораторы ===
def is_prime(func):
    def warp(*args, **kwargs):
        res_sum_three = func(*args, **kwargs)
        if res_sum_three <= 1 :
            return 'Число меньше одного или равные одному не являются простыми'
        for i in range(2, int(res_sum_three ** 0.5) + 1):
            if res_sum_three % i == 0:
                return f'{res_sum_three} - Число составное'
        return f'{res_sum_three} - Число простое'
    return warp

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
result2 = sum_three(3, 4, 8)
print(result2)
result3 = sum_three(1, 4, 2)
print(result3)
result4 = sum_three(8, 7, 44)
print(result4)
result5 = sum_three(1, 22, 13)
print(result5)
result6 = sum_three(4, 15, 5)
print(result6)
result7 = sum_three(1, 2, 2)
print(result7)
result8 = sum_three(1, 1, 1)
print(result8)