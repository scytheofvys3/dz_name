# === DZ 35 номер задания не терять
def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        res = i(int_list)
        # result = {i.__name__:res} # создает новый словарь на каждой итерации
        # result.update({i.__name__:res}) # обновляет словарь на каждой итерации
        result[i.__name__] = res # обновляет словарь, но если ключ совпадает, то он обновляет его значение
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
