import math
from time import time
from random import random


def insertion_sort(numbers):
    result = numbers[:] 
    for i in range(1, len(result)):
        j = i
        while j > 0 and result[j-1] > result[j]:
            temp = result[j]
            result[j] = result[j-1]
            result[j-1] = temp
            j -= 1

    return result


def radix_sort(numbers, k=pow(2, 16)):
    result = numbers[:]
    n = len(result)
    

    num_digits = int(math.ceil(math.log(k, n)))
    for i in range(num_digits):
        csr(result, i+1, n)

    return result

def csr(numbers, digit, n):
    arr = {}
    for i in numbers:
        index = get_digit(i, digit, n)

        arr[index] = arr.get(index, [])
        arr[index].append(i)

    count = 0
    for i in range(n):
        repetitions = arr.get(i, None)
        if(repetitions): 
            for value in repetitions:
                numbers[count] = value
                count += 1

def get_digit(num, d, k):
    l = int(math.ceil(math.log(num+1, k)))
    return num // pow(k, d-1) % k

    

def merge(left, right):
    i = 0
    j = 0
    result = []
    while True:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if(i >= len(left)):
            return result + right[j:]
        if(j >= len(right)):
            return result + left[i:]

def merge_sort(numbers):

    if len(numbers) == 1:
        return numbers

    split_point = len(numbers)//2

    left = merge_sort(numbers[:split_point])
    right = merge_sort(numbers[split_point:])

    return merge(left, right)

def quick_sort(numbers):
    if not len(numbers) or len(numbers) == 1:
        return numbers

    result = numbers[:]
        
    l = len(result)
    split_index = len(result)//2
    split_value = result[split_index]
    temp = result[split_index]
    result[split_index] = result[l-1]
    result[l-1] = temp

    i = 0
    j = len(result)-2
    stop = False
    while j >= i:
        while(result[i] > split_value):
            if j <= i:
                stop = True
                break
            temp = result[i]
            result[i] = result[j]
            result[j] = temp
            j -= 1
        if stop:
            break
        i += 1
    result[len(result)-1] = result[i]
    result[i] = split_value
    
    left = quick_sort(result[:i])
    right = quick_sort(result[i+1:])

    return left + [split_value] + right


def sort_check(numbers):
    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            print(numbers[i-1], numbers[i])
            assert False


def test_algorithm(algos, numbers, iterations=100):
    times = {}
    for i in range(iterations):
        for algo in algos:
            start = time()
            result = algo(numbers)
            end = time() - start
            times[algo.__name__] = times.get(algo.__name__, 0) + end 
            sort_check(result)

    for name, dt in times.items():
        dt /= iterations
        func_name = ' '.join(list(map(lambda x: x.capitalize(), name.split('_'))))
        print(f'{func_name:<20}  Time: {dt:.5f}')


# k = pow(2, 16)
# numbers = [int(random() * k) for i in range(20000)]

# test_algorithm([radix_sort, merge_sort, quick_sort], numbers)