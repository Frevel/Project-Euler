'''
Project Euler - Problem 1
2018-04-15 Frevel
'''

def sum_multiples(x):
    '''
    x (int) : upper limit
    Returns (int): the sum of all multiples of 3 and 5
    below x
    '''
    sum = 0
    for i in range(0, x, 3):
        if i % 5 != 0: sum += i
    for i in range(0, x, 5):
        sum += i
    return sum


print(sum_multiples(1000))
