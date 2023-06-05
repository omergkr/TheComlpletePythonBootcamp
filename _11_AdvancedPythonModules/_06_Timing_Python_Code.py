import time


def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


# Timing Start and Stop


# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result1 = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result2 = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)

# Timeit Module

import timeit

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
    '''

stmt = 'func_one(100)'
print(timeit.timeit(stmt, setup, number=100000))

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

stmt2 = 'func_two(100)'

print(timeit.timeit(stmt2, setup2, number=100000))


