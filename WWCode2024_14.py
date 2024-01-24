# Women Who Code (Python) Challenge No. 14
# Write a program to print the first n numbers of a Fibonacci sequence.

def fib_seq(n):
    fib = [0,1]

    for i in range(2,n):
        next_num = fib[i-1] + fib[i-2]
        fib.append(next_num)

    return fib[1:n]

n = int(input('Enter the value of n: '))
result = fib_seq(n)

print(f'First {n} numbers of Fibonacci sequence: {result}')
        
