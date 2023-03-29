from random import randint
def create_list(length):
    res = []
    for i in range(length):
        res.append(randint(-20, 20))
    return res
def find_index(lst, nrange):
    index_list = []
    for i in range(len(lst)):
        if nrange[0] <= lst[i] <= nrange[1]:
            index_list.append(i)
    return index_list




size = int(input("Введите размер списка: "))
num_range = [int(input(f"Введите {['минимальное', 'максимальное'][i]} число диапазона: ")) for i in range(2)]
nums = create_list(size)
print(nums)
print(find_index(nums, num_range))
