import random
import time
random.seed(0)

int_list = []
for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))


def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

bubble_sort(int_list)


def everage_time(lst, iter_number):
    total_time = 0
    for i in range(0, iter_number):
        start_time = time.time()
        i = lst
        end_time = time.time() - start_time
        total_time += end_time
    return total_time / iter_number

et = everage_time(bubble_sort(int_list), 50)
print(f"Everage time is {et} seconds")









