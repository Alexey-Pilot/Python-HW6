def arif_prog(first_num, step, size):
    res = []
    for i in range(first_num, first_num + step * size + 1, step):
        res.append(i)
    return res
s = ["первый элемент", "шаг", "длину"]
fnum, step, size = [int(input(f"Введите {s[i]} прогрессии: ")) for i in range(3)]
print(arif_prog(first_num=fnum, step=step, size=size))
