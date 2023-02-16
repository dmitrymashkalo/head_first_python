# Description: The task is to convert the three 'for' cycles into generators.

# Task 1
t1_data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for i in t1_data:
    if not i % 2:
        evens.append(i)

# Solution for task 1
evens2 = [i for i in t1_data if not i % 2]


# Task 2
t2_data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for i in t2_data:
    if isinstance(i, str):
        words.append(i)

# Solution for task 2
words2 = [i for i in t2_data if isinstance(i, str)]


# Task 3
t3_data = list('So long and thanks for all the fish'.split())
title = []
for i in t3_data:
    title.append(i.title())

# Solution for task 3
title2 = [i.title() for i in t3_data]
