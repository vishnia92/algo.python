# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков
def my_func(num_list):
    min_el = float('-inf')
    for i, item in enumerate(num_list):
        if min_el < item < 0:
            min_el = item
            min_idx = i


# python -m timeit -n 100 -s "import random" "x = [random.randint(-100, 0) for _ in range(10)]" "import task_1" "task_1.my_func(x)"

# 100 loops, best of 5: 72.4 usec per loop      random.randint(-10, 0) for _ in range(10)
# 100 loops, best of 5: 682 usec per loop       100
# 100 loops, best of 5: 76.4 usec per loop      random.randint(-100, 0) for _ in range(10)
# 100 loops, best of 5: 764 usec per loop       100
# 100 loops, best of 5: 7.86 msec per loop      1000
# 100 loops, best of 5: 67.8 msec per loop      10000
# 100 loops, best of 5: 673 msec per loop       100000



def func_2(num_list):
    new_list = [i for i in num_list if i < 0]
    maximum = max(new_list)
    idx = new_list.index(maximum)

# 100 loops, best of 5: 66.9 usec per loop      random.randint(-10, 10) for _ in range(10)
# 100 loops, best of 5: 612 usec per loop       100
# 100 loops, best of 5: 76.9 usec per loop      random.randint(-100, 100) for _ in range(10)
# 100 loops, best of 5: 632 usec per loop       100
# 100 loops, best of 5: 6.16 msec per loop      1000
# 100 loops, best of 5: 64.4 msec per loop      10000
# 100 loops, best of 5: 411 msec per loop       100000