def bubble_sort(num):
    n = len(num)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num
unsorted_list = [123, 734, 90, 666, 213, 444]
sorted_list = bubble_sort(unsorted_list.copy())

print("Неотсортированный список:", unsorted_list)
print("Отсортированный список:", sorted_list)


def binary_search(num_list, number):
    N = 5000
    ResultOk = False
    First = 0
    Last = N - 1
    pos = -1

    while First <= Last and not ResultOk:
        Middle = (First + Last) // 2
        if num_list[Middle] == number:
            ResultOk = True
            pos = Middle
            First = Middle
            Last = First
        elif num_list[Middle] < number:
            First = Middle + 1
        else:
            Last = Middle - 1

    return pos if 0 <= pos < N else -1
N = 5000
num_list = sorted_list
number = 444
print(f"Number {number} found in {num_list}")



